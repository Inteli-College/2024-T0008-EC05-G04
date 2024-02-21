import json
import typer
import inquirer
from yaspin import yaspin

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
@yaspin(text="Homing the robot...")
def home(
    wait: Annotated[bool, typer.Option(help="Wait for the robot to reach home")] = True,
):
    """
    Move to the home position
    """
    dobot_controller.home(wait)


@app.command()
@yaspin(text="Enabling the tool...")
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
@yaspin(text="Disabling the tool...")
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
        spinner = yaspin(text=f"Moving to {position}...")
        current_position = Position()
        current_position.load_from_dict(position)
        dobot_controller.move_to(current_position, wait=True)
        spinner.stop()


@app.command()
def control():
    """
    Open the control interface
    """
    command = inquirer.prompt(
        [
            inquirer.List(
                "command",
                message="Select the command",
                choices=[
                    "Move",
                    "Move to",
                    "Home",
                    "Enable tool",
                    "Disable tool",
                    "Current",
                    "Save",
                    "Run",
                ],
            )
        ]
    ).get("command")

    command_map = {
        "Move": move,
        "Move to": move_to,
        "Home": home,
        "Enable tool": enable_tool,
        "Disable tool": disable_tool,
        "Current": current,
        "Save": save,
        "Run": run,
    }

    args = {
        "Move": ["axis", "distance", "wait"],
        "Move to": ["x", "y", "z", "r", "wait"],
        "Home": ["wait"],
        "Enable tool": ["time_to_wait"],
        "Disable tool": ["time_to_wait"],
        "Save": ["file_path"],
        "Run": ["file_path"],
    }

    types = {
        "Move": [str, float, bool],
        "Move to": [float, float, float, float, bool],
        "Home": [bool],
        "Enable tool": [int],
        "Disable tool": [int],
        "Save": [str],
        "Run": [str],
    }

    command_args = args.get(command)

    if not command_args:
        command_map[command]()
        return

    command_args = [
        typer.prompt(
            f"Enter the {arg}", type=types[command][index], show_default=False
        )
        for index, arg in enumerate(command_args)
    ]

    command_map[command](*command_args)

def main():
    available_ports = dobot_controller.list_ports()

    port = inquirer.prompt(
        [inquirer.List("port", message="Select the port", choices=available_ports)]
    ).get("port")

    spinner = yaspin(text=f"Connecting with port {port}...")
    spinner.start()
    dobot_controller.connect(port)
    spinner.stop()

    app()


if __name__ == "__main__":
    main()
