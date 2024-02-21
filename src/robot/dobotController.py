from serial.tools import list_ports
import mock_pydobot as pydobot
import json

from position import Position


class DobotController:
    def __init__(self):
        self.tool_enabled = False
        self.home_position = Position(240, 0, 150, 0, 0, 0, 0, 0, False, False)

    def list_ports(self):
        if hasattr(pydobot.Dobot, "__mocked__"):
            print("mock")
            return pydobot.mocked_ports

        return list_ports.comports()

    def connect(self, port_name):
        self.dobot = pydobot.Dobot(port=port_name.device, verbose=False)

    def pose(self):
        current_position = Position(*self.dobot.pose())
        current_position.suction = self.tool_enabled
        return current_position

    def move_to(self, position, wait=True):
        print(f"Moving to {position}")
        self.dobot.move_to(*position.to_list(), wait=wait)

    def move_by_axis(self, axis, distance, wait):
        move = Position(
            x=distance * (axis == "x"),
            y=distance * (axis == "y"),
            z=distance * (axis == "z"),
            r=distance * (axis == "r"),
        )

        target_position = self.pose() + move

        self.move_to(target_position, wait=wait)

    def execute_positions(self, data):
        current_position = Position()

        for position in data["positions"]:
            current_position.load_from_dict(position)
            self.move_to(current_position, wait=True)

    def save_current_position(self, path):
        current_position = self.pose()
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
        self.move_to(self.home_position, wait=True)

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
        current_position = self.pose()
        print(current_position)
