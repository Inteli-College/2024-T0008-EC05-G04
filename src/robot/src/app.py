from flask import Flask, request
from flask_cors import CORS
import inquirer
from yaspin import yaspin

from dobotController import DobotController
from position import Position

ROBOT_ID = "001"

dobot_controller = DobotController()

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


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/move", methods=["POST"])
def move_linear():
    data = request.json
    target_position = parse_position(data)
    dobot_controller.move_to(target_position, wait=data.get("wait", True))

    return "ok"


# execute


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
