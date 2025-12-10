from vector2D import Vector2Math
import math

GRAVITY = Vector2Math(12, x=0, y=-9.81)

class KinematicsBody():
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration


    def update(self, dt):
        self.velocity = self.velocity + self.acceleration * dt
        self.position = self.position + self.velocity * dt

    def displacement_after_time(self, dt):
        return (self.velocity * dt) + (0.5 * self.acceleration * dt**2)

    def velocity_after_time(self, dt):
        return self.velocity + self.acceleration * dt

    def position_after_time(self, dt):
        return self.position + self.displacement_after_time(dt)

    def add_acceleration(self, adding_acceleration):
        self.acceleration = self.acceleration + adding_acceleration




