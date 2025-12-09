import math
import numpy


class Vector2Math:
    """
    Code by Arjun Agarwal.
    All angles are in degrees, conversions done inside code.
    """

    def __init__(self, x_component, y_component):
        self.x = x_component
        self.y = y_component

    def get_vector(self):
        return (self.x, self.y)

    @property
    def magnitude(self):
        return self.pythagorean_theorem(self.x, self.y)

    @property
    def angle(self):
        return self.calculate_angle(self.x, self.y)

    @property
    def vector(self):
        return self.get_vector()
    @staticmethod
    def pythagorean_theorem(x_component, y_component):
        return math.sqrt(x_component**2 + y_component**2)

    @staticmethod
    def calculate_xy_components(angle, hypot):
        angle = math.radians(angle)
        y_component = hypot * math.sin(angle)
        x_component = hypot * math.cos(angle)
        return x_component, y_component

    @staticmethod
    def calculate_hypot(x_component, y_component):
        return Vector2Math.pythagorean_theorem(x_component, y_component)

    @staticmethod
    def calculate_angle(x_component, y_component):
        return math.degrees(math.atan2(y_component, x_component))

    @classmethod
    def from_angle_and_hypot(cls, angle, hypot):
        x, y = cls.calculate_xy_components(angle, hypot)
        return cls(x, y)

    @classmethod
    def from_points(cls, x1, y1, x2, y2):
        return cls(x2 - x1, y2 - y1)

    def __add__(self, b):
        return Vector2Math(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Vector2Math(self.x - b.x, self.y - b.y)

    def __repr__(self):
        return f"Vector2Math({self.x}, {self.y})"


a = Vector2Math(8.7, 5)
b = Vector2Math(0, 5)
c = a - b
print(c.vector)

