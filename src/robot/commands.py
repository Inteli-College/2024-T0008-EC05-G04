from abc import ABC, abstractmethod
import json

from dobotController import DobotController
from position import Position


def read_position_from_file(path):
    with open(path, "r") as file:
        data = json.load(file)

    position = Position()
    position.load_from_dict(data)

    return position


def read_position_data_from_file(path):
    with open(path, "r") as file:
        data = json.load(file)

    return data


class Command(ABC):
    def __init__(self, dobot_controller):
        self.dobot_controller = dobot_controller

    @abstractmethod
    def execute(self, args):
        pass


class MoveCommand(Command):
    def execute(self, args):
        if len(args) < 3:
            print("Usage: move <axis> <distance> [<wait>]")
            return

        axis, distance, wait = (
            args[1],
            float(args[2]),
            args[3] if len(args) > 3 else False,
        )

        self.dobot_controller.move_by_axis(axis, distance, wait)


class MoveToCommand(Command):
    def execute(self, args):
        if len(args) < 2:
            print("Usage: move_to <path>")
            return

        path = args[1]
        position = read_position_from_file(path)
        self.dobot_controller.move_to_position(position)


class ExecuteCommand(Command):
    def execute(self, args):
        if len(args) < 2:
            print("Usage: execute <path>")
            return

        path = args[1]
        data = read_position_data_from_file(path)
        self.dobot_controller.execute_positions(data)


class SavePositionCommand(Command):
    def execute(self, args):
        if len(args) < 2:
            print("Usage: save <path>")
            return

        path = args[1]
        self.dobot_controller.save_current_position(path)


class HomeCommand(Command):
    def execute(self, args):
        self.dobot_controller.home()


class EnableToolCommand(Command):
    def execute(self, args):
        self.dobot_controller.enable_tool()


class DisableToolCommand(Command):
    def execute(self, args):
        self.dobot_controller.disable_tool()


class GetCurrentPositionCommand(Command):
    def execute(self, args):
        self.dobot_controller.get_current_position()
