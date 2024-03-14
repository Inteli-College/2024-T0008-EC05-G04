from flask import Flask, request
from flask_cors import CORS
import inquirer
from yaspin import yaspin
import json

from dobotController import DobotController
from position import Position

ROBOT_ID = "001"

dobot_controller = DobotController()

with open("home.json") as file:
    home = json.load(file)

app = Flask(__name__)
CORS(app)


def parse_position(data):
    return Position(
        data.get("x", 0),
        data.get("y", 0),
        data.get("z", 0),
        data.get("r", 0),
        data.get("j1", 0),
        data.get("j2", 0),
        data.get("j3", 0),
        data.get("j4", 0),
        data.get("grip", False),
        data.get("suction", False),
        data.get("linear", False),
    )

def register_robot():
    # registra o robô no backend
    pass

def move_item(item):
    #moveu para posição de segurança, somente Z é não é alterado
    dobot_controller.move_to(Position(item.get("X"), item.get("Y"),
    dobot_controller.home_z, item.get("R"), linear=False), wait=200)

    #moveu para o objeto, somente Z é alterado
    dobot_controller.move_to(Position(item.get("X"), item.get("Y"),
    item.get("Z"), item.get("R"), linear=True), wait=200)

    #liga ferramenta
    dobot_controller.enable_tool()

    #verifica se pegou o objeto
    caught_object = await receive_signal()
    if caught_object:
        dobot_controller.move_to(Position(item.get("X"), item.get("Y"),
        dobot_controller.home_z, item.get("R"),linear=True), wait=200)
        dobot_controller.move_to(Position(20, 0, 150, 0, linear=False), wait=200)
        dobot_controller.move_to(Position(20, 0, 0, 0, linear=True), wait=200)
        dobot_controller.move_to(Position(20, 0, 150, 0, linear=True),wait=200)
        dobot_controller.home()
        return True
    return False

#endpoint para montar kit
@app.route('/make-kits')
def try_caught_object(item_list):
    #carregando json para o objeto
    itens_kit = item_list.loads()
    for item in itens_kit.positions:
        resultado = move_item(item)
        if not resultado:
            for i in range(3):
                resultado = move_item(item)
                if resultado:
                    break 
        
@app.get('/raspberry', methods=['POST'])
def receive_signal (sensor_value):
    return sensor_value > 25000 
    
# sinal< 25000
if __name__ == "__main__":
    available_ports = dobot_controller.list_ports()
    port = inquirer.prompt(
        [inquirer.List("port", message="Select the port", choices=available_ports)]
    ).get("port")

    spinner = yaspin(text=f"Connecting with port {port}...")
    spinner.start()
    dobot_controller.connect(port)
    spinner.stop()

    register_robot()
    app.run(debug=True, host="0.0.0.0", port=5000)
