from serial.tools import list_ports
import pydobot
import json

from position import Position


class DobotController:
    def __init__(self):
        available_ports = list_ports.comports()
        port = list(available_ports)[0].device
        self.dobot = pydobot.Dobot(port=port, verbose=False)

        self.tool_enabled = False
        self.dobot.suck(self.tool_enabled)
        self.home_position = Position(240, 0, 150, 0, 0, 0, 0, 0, False, False)

    def pose(self):
        return self.dobot.pose()

    def move_by_axis(self, current_position, axis, distance, wait):
        move = Position(
            x=distance * (axis == "x"),
            y=distance * (axis == "y"),
            z=distance * (axis == "z"),
        )

        target_position = current_position + move

        self.dobot.move_to(*target_position.to_list(), wait=wait)

    def move_to_position(self, position):
        print(f"Moving to {position}")
        self.dobot.move_to(*position.to_list())

    def execute_positions(self, data):
        current_position = Position()

        for position in data["positions"]:
            current_position.load_from_dict(position)

            print(current_position)

            self.dobot.move_to(*current_position.to_list(), wait=True)

    def save_current_position(self, path):
        current_position = Position(*self.dobot.pose())
        current_position.suction = self.tool_enabled
        print(current_position)

        try:
            with open(path, "r") as file:
                saved_positions = json.load(file)
        except FileNotFoundError:
            saved_positions = {"positions": []}

            with open(path, "w") as file:
                json.dump(saved_positions, file)

        saved_positions["positions"].append(current_position.to_dict())
        with open(path, "w") as file:
            json.dump(saved_positions, file, indent=4)

    def home(self):
        print("Homing robot")
        self.dobot.move_to(*self.home_position.to_list())

    def enable_tool(self):
        print("Enabling tool")
        self.dobot.suck(True)
        self.tool_enabled = True

    def disable_tool(self):
        print("Disabling tool")
        self.dobot.suck(False)
        self.tool_enabled = False

    def get_current_position(self):
        print("Getting current position")
        current_position = Position(*self.dobot.pose())
        current_position.suction = self.tool_enabled
        print(current_position)
