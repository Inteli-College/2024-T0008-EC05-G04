from flask import Flask, request
from flask_cors import CORS
import inquirer
from yaspin import yaspin
import json
import time

from dobotController import DobotController
from position import Position

ROBOT_ID = "001"
SAFE_Z_TRESHOLD = 80
BAG_POSITION = Position(
    121.5785140991211,
    -248.98097229003906,
    80.80499267578125,
    -63.973541259765625,
)

dobot_controller = DobotController()

app = Flask(__name__)
CORS(app)

with open("calibration.json") as file:
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
    pass


def move_item(item_position):
    item_position.z += SAFE_Z_TRESHOLD
    dobot_controller.move_to(
        item_position,
        wait=True,
    )

    item_position.z -= SAFE_Z_TRESHOLD

    dobot_controller.move_to(
        item_position,
        wait=True,
    )

    print("catching")

    dobot_controller.enable_tool()

    timeout = time.time() + 5
    while not dobot_controller.caught_object:
        time.sleep(0.5)
        if time.time() > timeout:
            print("fail to catch")
            return False

    print("gotcha")

    item_position.z += SAFE_Z_TRESHOLD

    dobot_controller.move_to(
        item_position,
        wait=True,
    )

    time.sleep(1)

    if not dobot_controller.caught_object:
        print("fail to catch")
        return False

    dobot_controller.move_to(BAG_POSITION, wait=True)

    dobot_controller.disable_tool()
    dobot_controller.home()

    return True


@app.route("/kit-order", methods=["POST"])
def try_caught_object():
    kit_order = request.json

    itens = kit_order.get("kit").get("itens")

    for item in itens:
        item_position = str(item.get("item_position"))
        raw_position = positions[item_position]

        position = Position(
            raw_position.get("x"), raw_position.get("y"), raw_position.get("z")
        )

        catched = False
        try_counts = 0
        while not catched:
            catched = move_item(position)

            try_counts += 1
            if try_counts > 3:
                break

    return "OK"


@app.route("/raspberry-feed", methods=["POST"])
def receive_signal():
    sensor_value = request.json.get("sensor_value")
    sensor_value = int(sensor_value)
    print(sensor_value)
    dobot_controller.set_caught_object(sensor_value < 25000)
    return "OK"


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
