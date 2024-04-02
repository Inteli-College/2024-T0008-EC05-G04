from pydobot.enums import PTPMode

__mocked__ = True


class MockedSerial:
    device = "mock"


mocked_serial = MockedSerial()


class Dobot:
    def __init__(self, port, verbose=False):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 0
        self.j1 = 0
        self.j2 = 0
        self.j3 = 0
        self.j4 = 0
        self.suction_enabled = False
        print(f"Connecting to Dobot on port {port}")

    def close(self):
        print("Closing connection to Dobot")

    def _set_ptp_cmd(self, x, y, z, r, mode, wait):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

        print("Moving ", end="")

        if mode == PTPMode.MOVL_XYZ:
            print("linearly", end="")

        print(f" to ({x}, {y}, {z}, {r})", end="")

        if wait:
            print(" and waiting")

        print()

    def suck(self, enable):
        print(f"Sucking {enable}")
        self.suction_enabled = enable

    def grip(self, enable):
        print(f"Gripping {enable}")
        self.grip_enabled = enable

    def speed(self, velocity=100.0, acceleration=100.0):
        print(
            f"Setting speed to {velocity} mm/s and acceleration to {acceleration} mm/s^2"
        )

    def wait(self, ms):
        print(f"Waiting for {ms} ms")

    def pose(self):
        return (self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4)
