import typer
import inquirer

from typing_extensions import Annotated
from dobotController import DobotController
from position import Position

app = typer.Typer()
dobot_controller = DobotController()


@app.command()
def move(
    axis: Annotated[str, typer.Argument(help="Axis to move")],
    distance: Annotated[float, typer.Argument(help="Distance to move the axis")],
    wait: Annotated[bool, typer.Option(help="Wait for the movement to finish")] = True,
):
    """
    Move the robot by a specific distance
    """
    dobot_controller.move_by_axis(axis, distance, wait)


@app.command()
def move_to(
    x: Annotated[float, typer.Argument(help="X coordinate to move to")],
    y: Annotated[float, typer.Argument(help="Y coordinate to move to")],
    z: Annotated[float, typer.Argument(help="Z coordinate to move to")],
    r: Annotated[float, typer.Argument(help="R coordinate to move to")],
    wait: Annotated[bool, typer.Option(help="Wait for the movement to finish")] = True,
):
    """
    Move to a specific position
    """
    dobot_controller.move_to(Position(x, y, z, r), wait)


@app.command()
def home(
    wait: Annotated[bool, typer.Option(help="Wait for the robot to reach home")] = True,
):
    """
    Move to the home position
    """
    dobot_controller.home(wait)


@app.command()
def enable_tool(
    time_to_wait: Annotated[
        int, typer.Option(help="Time to wait for the tool to enable")
    ] = 200,
):
    """
    Enable the tool
    """
    dobot_controller.enable_tool(time_to_wait)


@app.command()
def disable_tool(
    time_to_wait: Annotated[
        int, typer.Option(help="Time to wait for the tool to disable")
    ] = 200,
):
    """
    Disable the tool
    """
    dobot_controller.disable_tool(time_to_wait)


@app.command()
def current():
    """
    Print the current position
    """
    print(dobot_controller.pose())


@app.command()
def save(
    file_path: Annotated[str, typer.Argument(help="Path to save the current position")],
):
    """
    Save the current position to a file
    """
    current_position = dobot_controller.pose()

    try:
        with open(file_path, "r") as file:
            saved_positions = json.load(file)
    except FileNotFoundError:
        saved_positions = {"positions": []}

    with open(file_path, "w") as file:
        saved_positions["positions"].append(current_position.to_dict())
        json.dump(saved_positions, file, indent=4)


@app.command()
def run(
    file_path: Annotated[str, typer.Argument(help="Path to the file with positions")],
):
    """
    Execute a list of positions from a file
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    for position in data["positions"]:
        current_position = Position()
        current_position.load_from_dict(position)
        dobot_controller.move_to(current_position, wait=True)


def main():
    available_ports = dobot_controller.list_ports()

    port = inquirer.prompt(
        [inquirer.List("port", message="Select the port", choices=available_ports)]
    ).get("port")

    dobot_controller.connect(port)

    app()


if __name__ == "__main__":
    main()
