import json

from flask import copy_current_request_context
import typer
import inquirer
from yaspin import yaspin

from typing_extensions import Annotated
from dobotController import DobotController
from position import Position

app = typer.Typer()
dobot_controller = DobotController()


@app.command()
@yaspin(text="Moving the robot...")
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
@yaspin(text="Moving the robot...")
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
def calibrate():
    """
    Calibrate the robot
    """
    positions = {}
    number_of_positions = typer.prompt(
        "Enter the number of positions to calibrate", type=int
    )

    for i in range(number_of_positions):
        typer.echo(f"\nMove the robot to the desired {i+1}ª position")
        input("Press Enter when ready...")

        current_position = dobot_controller.pose()
        print(current_position)
        positions.update({i: current_position.to_dict()})

    typer.echo("Move the robot to the target position")
    input("Press Enter when ready...")

    positions.update({"target": dobot_controller.pose().to_dict()})

    typer.echo("\nCalibration finished!\n")

    file_path = typer.prompt("Enter the file path to save the calibration", type=str)

    print(positions)

    with open(file_path, "w") as file:
        json.dump(positions, file, indent=4)


@app.command()
def test_calibration():
    """
    Test the calibration
    """

    home()

    file_path = typer.prompt("Enter the file path with the calibration", type=str)

    with open(file_path, "r") as file:
        data = json.load(file)

    for key, value in data.items():
        if key == "target":
            continue

        spinner = yaspin(text=f"Moving to {key}...")
        spinner.start()
        current_position = Position()
        current_position.load_from_dict(value)

        current_position.z += 80
        dobot_controller.move_to(current_position, wait=True)
        current_position.z -= 80
        dobot_controller.move_to(current_position, wait=True)
        current_position.z += 80
        dobot_controller.move_to(current_position, wait=True)

        spinner.stop()

    spinner = yaspin(text="Moving to the home position...")
    dobot_controller.move_to(Position(0, 0, 0, 0), wait=True)
    spinner.stop()

    spinner = yaspin(text="Moving to the target position...")
    target_position = Position()
    target_position.load_from_dict(data["target"])
    target_position.z += 80
    dobot_controller.move_to(target_position, wait=True)
    target_position.z -= 80
    dobot_controller.move_to(target_position, wait=True)
    spinner.stop()


@app.command()
def control():
    """
    Open the control interface
    """
    loop = True
    while loop:
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
                        "Quit",
                    ],
                )
            ]
        ).get("command")

        if command == "Quit":
            loop = False
            continue

        if command == "Move":
            axis = inquirer.prompt(
                [
                    inquirer.List(
                        "axis",
                        message="Select the axis",
                        choices=["x", "y", "z", "r"],
                    )
                ]
            ).get("axis")
            distance = typer.prompt("Enter the distance", type=float)
            wait = typer.confirm("Wait for the movement to finish")
            move(axis, distance, wait)

        if command == "Move to":
            x = typer.prompt("Enter the x coordinate", type=float)
            y = typer.prompt("Enter the y coordinate", type=float)
            z = typer.prompt("Enter the z coordinate", type=float)
            r = typer.prompt("Enter the r coordinate", type=float)
            wait = typer.confirm("Wait for the movement to finish")
            move_to(x, y, z, r, wait)

        if command == "Home":
            wait = typer.confirm("Wait for the robot to reach home")
            home(wait)

        if command == "Enable tool":
            time_to_wait = typer.prompt(
                "Enter the time to wait for the tool to enable", type=int
            )
            enable_tool(time_to_wait)

        if command == "Disable tool":
            time_to_wait = typer.prompt(
                "Enter the time to wait for the tool to disable", type=int
            )
            disable_tool(time_to_wait)

        if command == "Current":
            current()

        if command == "Save":
            file_path = typer.prompt("Enter the file path", type=str)
            save(file_path)

        if command == "Run":
            file_path = typer.prompt("Enter the file path", type=str)
            run(file_path)


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
