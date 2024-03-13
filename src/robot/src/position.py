class Position:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        r: float = 0,
        j1: float = 0,
        j2: float = 0,
        j3: float = 0,
        j4: float = 0,
        grip: bool = False,
        suction: bool = False,
        linear: bool = False,
    ):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.j4 = j4
        self.grip = grip
        self.suction = suction
        self.linear = linear

    def load_from_dict(self, data):
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.r = data["r"]
        self.j1 = data["j1"]
        self.j2 = data["j2"]
        self.j3 = data["j3"]
        self.j4 = data["j4"]
        self.grip = data.get("grip", False)
        self.suction = data.get("suction", False)
        self.linear = data.get("linear", False)

    def load_from_list(self, data):
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]
        self.r = data[3]
        self.j1 = data[4]
        self.j2 = data[5]
        self.j3 = data[6]
        self.j4 = data[7]
        self.grip = data[8]
        self.suction = data[9]
        self.linear = data[10]

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "r": self.r,
            "j1": self.j1,
            "j2": self.j2,
            "j3": self.j3,
            "j4": self.j4,
            "grip": self.grip,
            "suction": self.suction,
            "linear": self.linear,
        }

    def to_list(self):
        return [self.x, self.y, self.z, self.r]

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}, r: {self.r}, j1: {self.j1}, j2: {self.j2}, j3: {self.j3}, j4: {self.j4}, grip: {self.grip}, suction: {self.suction}, linear: {self.linear}"

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}, r: {self.r}, j1: {self.j1}, j2: {self.j2}, j3: {self.j3}, j4: {self.j4}, grip: {self.grip}, suction: {self.suction}, linear: {self.linear}"

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.z == other.z
            and self.r == other.r
            and self.j1 == other.j1
            and self.j2 == other.j2
            and self.j3 == other.j3
            and self.j4 == other.j4
            and self.grip == other.grip
            and self.suction == other.suction
            and self.linear == other.linear
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Position(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.r + other.r,
            self.j1 + other.j1,
            self.j2 + other.j2,
            self.j3 + other.j3,
            self.j4 + other.j4,
        )

    def __sub__(self, other):
        return Position(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.r - other.r,
            self.j1 - other.j1,
            self.j2 - other.j2,
            self.j3 - other.j3,
            self.j4 - other.j4,
        )

    def __mul__(self, other):
        return Position(
            self.x * other,
            self.y * other,
            self.z * other,
            self.r * other,
            self.j1 * other,
            self.j2 * other,
            self.j3 * other,
            self.j4 * other,
        )
