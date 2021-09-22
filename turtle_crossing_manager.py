from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.speed_factor = 1

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(280, random.randint(-250,250))
        self.all_cars.append(new_car)

    def move(self):
        for i in range(len(self.all_cars)):
            self.all_cars[i].goto(self.all_cars[i].xcor() - MOVE_INCREMENT, self.all_cars[i].ycor())

    def increase_speed(self):
        self.speed_factor += MOVE_INCREMENT
