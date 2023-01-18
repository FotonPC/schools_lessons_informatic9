import math
import random
import numpy as np


class Car:
    def __init__(self, x=0, y=0, direction=0, L=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.L = L

    def __str__(self):
        return f"x: {self.x}, y: {self.y}; direction: {self.direction}, L: {self.L}"

    def move(self, time=0.0, speed=0.0):
        distance = time * speed
        rad_angle = math.radians(self.direction)
        self.x += math.cos(rad_angle) * distance
        self.y += math.sin(rad_angle) * distance
        self.L += distance

    def turn(self, angle=0.0):
        self.direction += angle

    def distance(self, x=0, y=0):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


if __name__ == "__main__":

    car = Car(0, 0, 0, 0)
    cmd_raw = input("car << ").lower()
    cmd_argues = cmd_raw.split()
    cmd = cmd_argues[0]
    while cmd_argues[0] != 'q':
        if cmd == 'm':
            time: float = float(cmd_argues[1])
            speed = float(cmd_argues[2])
            car.move(time=time, speed=speed)
            print("Car moved")

        if cmd == 't':
            angle = float(cmd_argues[1])
            car.turn(angle)
            print("Car turned")

        if cmd == 'l':
            print(f"Path length: {car.L}")

        if cmd == 'c':
            print(f"Car coordinates: x = {car.x}, y = {car.y}")

        if cmd == 'd':
            x = float(cmd_argues[1])
            y = float(cmd_argues[2])
            print(f"Car distance to point: {car.distance(x, y)}")

        if cmd == 's':
            print(car)

        cmd_raw = input("car << ").lower()
        cmd_argues = cmd_raw.split()
        cmd = cmd_argues[0]
