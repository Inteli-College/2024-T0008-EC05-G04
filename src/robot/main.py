from commands import *

command_mapping = {
    "move": MoveCommand(),
    "move_to": MoveToCommand(),
    "execute": ExecuteCommand(),
    "save": SavePositionCommand(),
    "home": HomeCommand(),
    "enable_tool": EnableToolCommand(),
    "disable_tool": DisableToolCommand(),
    "current": GetCurrentPositionCommand(),
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
