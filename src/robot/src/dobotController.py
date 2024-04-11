from serial.tools import list_ports
import pydobot
from pydobot.enums import PTPMode
import mock_pydobot

from position import Position


class DobotController:
    def __init__(self):
        self.tool_enabled = False
        self.home_position = Position(240, 0, 150, 0, 0, 0, 0, 0, False, False)
        self.caught_object = False

    def list_ports(self):
        ports = ["mock"]
        ports += [port.device for port in list_ports.comports()]

        return ports

    def connect(self, port):
        if port == "mock":
            self.dobot = mock_pydobot.Dobot(port=port, verbose=False)
            return

        self.dobot = pydobot.Dobot(port=port, verbose=False)

    def disconnect(self):
        self.dobot.close()

    def pose(self):
        current_position = Position(*self.dobot.pose())
        current_position.suction = self.tool_enabled
        return current_position

    def move_linear(self, position, wait=True):
        self.dobot._set_ptp_cmd(
            position.x,
            position.y,
            position.z,
            position.r,
            mode=PTPMode.MOVL_XYZ,
            wait=wait,
        )

    def move_joint(self, position, wait=True):
        self.dobot._set_ptp_cmd(
            position.x,
            position.y,
            position.z,
            position.r,
            mode=PTPMode.MOVJ_XYZ,
            wait=wait,
        )

    def move_to(self, position, wait=True):
        if position.linear:
            self.move_linear(position, wait=wait)
            return

        self.move_joint(position, wait=wait)

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

    def home(self, wait=True):
        self.move_to(self.home_position, wait=wait)

    def enable_tool(self, time_to_wait=200):
        self.dobot.suck(True)
        self.dobot.wait(time_to_wait)
        self.tool_enabled = True

    def disable_tool(self, time_to_wait=200):
        self.dobot.suck(False)
        self.dobot.wait(time_to_wait)
        self.tool_enabled = False

    def set_caught_object(self, status):
        self.caught_object = status
