import math


class Vector2Math:
    """
    Code by Arjun Agarwal.
    All angles are in degrees, conversions done inside code.
    """

    def __init__(self, decimals, x=None, y=None, angle=None, hypot=None):
        self.DECIMALS = decimals
        if angle is not None and hypot is not None:
            self.x = round(hypot * math.cos(math.radians(angle)), self.DECIMALS)
            self.y = round(hypot * math.sin(math.radians(angle)), self.DECIMALS)
        elif x is not None and y is not None:
            self.x = round(x, self.DECIMALS)
            self.y = round(y, self.DECIMALS)
        else:
            raise ValueError("Must provide either x and y, or angle and hypot")

    @property
    def vector(self):
        return (self.x, self.y)

    @property
    def magnitude(self):
        return round(math.sqrt(self.x**2 + self.y**2), self.DECIMALS)

    @property
    def angle(self):
        return round(math.degrees(math.atan2(self.y, self.x)), self.DECIMALS)

    def __add__(self, b):
        return Vector2Math(self.DECIMALS, round(self.x + b.x, self.DECIMALS), round(self.y + b.y, self.DECIMALS))

    def __sub__(self, b):
        return Vector2Math(self.DECIMALS, round(self.x - b.x, self.DECIMALS), round(self.y - b.y, self.DECIMALS))

    def __repr__(self):
        return f"Vector2Math({self.x}, {self.y})"
