from flask import Flask, request
from flask_cors import CORS
import inquirer
from yaspin import yaspin
import json
import time

from dobotController import DobotController
from position import Position

ROBOT_ID = "001"

dobot_controller = DobotController()

app = Flask(__name__)
CORS(app)

with open("positions.json") as file:
    positions = json.load(file)


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
    # moveu para posição de segurança, somente Z é não é alterado
    dobot_controller.move_to(
        Position(
            item.get("x"),
            item.get("y"),
            item.get("z") + 120,
            item.get("r"),
            linear=False,
        ),
        wait=200,
    )

    # moveu para o objeto, somente Z é alterado
    dobot_controller.move_to(
        Position(
            item.get("x"), item.get("y"), item.get("z"), item.get("r"), linear=True
        ),
        wait=200,
    )

    # liga ferramenta
    print("catching")
    dobot_controller.enable_tool()

    timeout = time.time() + 10
    while not dobot_controller.caught_object:
        time.sleep(0.5)
        if time.time() > timeout:
            print("fail to catch")
            return False

    print("gotcha")

    dobot_controller.move_to(
        Position(
            item.get("x"),
            item.get("y"),
            item.get("z") + 120,
            item.get("r"),
            linear=True,
        ),
        wait=200,
    )
    dobot_controller.move_to(
        (
            Position(
                121.5785140991211,
                -248.98097229003906,
                80.80499267578125,
                -63.973541259765625,
            )
        ),
        wait=200,
    )
    dobot_controller.disable_tool()
    dobot_controller.home()

    return True


# endpoint para montar kit
@app.route("/kit-order", methods=["POST"])
def try_caught_object():
    # carregando json para o objeto
    itens_kit_json = json.loads(request.json)
    for item in itens_kit_json:
        position = str(item.get("position"))
        item = positions[position]
        resultado = move_item(item)
        if not resultado:
            for i in range(3):
                resultado = move_item(item)
                if resultado:
                    break
    return "OK"


@app.route("/raspberry-feed", methods=["POST"])
def receive_signal():
    sensor_value = request.json.get("sensor_value")
    sensor_value = int(sensor_value)
    print(sensor_value)
    dobot_controller.set_caught_object(sensor_value < 25000)
    return "OK"


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
