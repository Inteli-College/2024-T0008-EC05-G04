from serial.tools import list_ports
import mock_pydobot as pydobot

from position import Position


class DobotController:
    def __init__(self):
        self.tool_enabled = False
        self.home_position = Position(240, 0, 150, 0, 0, 0, 0, 0, False, False)

    def list_ports(self):
        ports = [port.device for port in list_ports.comports()]

        if hasattr(pydobot, "__mocked__"):
            print('mock')
            ports.append("mock")

        return ports

    def connect(self, port):
        self.dobot = pydobot.Dobot(port=port, verbose=False)

    def disconnect(self):
        self.dobot.close()

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

    def home(self):
        print("Homing robot")
        self.move_to(self.home_position, wait=True)

    def enable_tool(self, time_to_wait=200):
        print("Enabling tool")
        self.dobot.suck(True)
        self.dobot.wait(time_to_wait)
        self.tool_enabled = True

    def disable_tool(self, time_to_wait=200):
        print("Disabling tool")
        self.dobot.suck(False)
        self.dobot.wait(time_to_wait)
        self.tool_enabled = False
