from flask import Flask
from typing_extensions import Annotated
from dobotController import DobotController
from position import Position
import json

dobot_controller = DobotController()

available_ports = dobot_controller.list_ports()

port = inquirer.prompt(
    [inquirer.List("port", message="Select the port", choices=available_ports)]
).get("port")
dobot_controller.connect(port)

while True:
    pass


# Fazer os kits
def make_kits(item_list):
        items_kit = item_list.loads()
        for item in items_kit:
            dobot_controller.move_to(Position(item.position.get("X"), item.position.get("Y"), 
            dobot_controller.home_position.z, item.position.get("R")), wait)
            
            dobot_controller.move_to(Position(item.position.get("X"), item.position.get("Y"), 
            item.position.get("Z"), item.position.get("R")), wait)
            
            dobot_controller.enable_tool()

            dobot_controller.move_to(Position(item.position.get("X"), item.position.get("Y"), 
            dobot_controller.home_position.z, item.position.get("R")), wait)
            
            dobot_controller.home()
            
