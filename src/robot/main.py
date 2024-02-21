from commands import *
from dobotController import DobotController

dobot_controller = DobotController()
available_ports = dobot_controller.list_ports()
dobot_controller.connect(available_ports[0])

command_mapping = {
    "move": MoveCommand(dobot_controller),
    "move_to": MoveToCommand(dobot_controller),
    "execute": ExecuteCommand(dobot_controller),
    "save": SavePositionCommand(dobot_controller),
    "home": HomeCommand(dobot_controller),
    "enable_tool": EnableToolCommand(dobot_controller),
    "disable_tool": DisableToolCommand(dobot_controller),
    "current": GetCurrentPositionCommand(dobot_controller),
}


def main():
    while True:
        user_command = input(": ")
        user_command = user_command.split(" ")

        if user_command[0] in ["exit", "quit", "q"]:
            break

        command_name = user_command[0]
        command = None

        command = command_mapping.get(command_name, None)

        if command is None:
            print("Available commands:")
            print("\n".join(command_mapping.keys()))
            continue

        command.execute(user_command)


if __name__ == "__main__":
    main()
