from turtle import Turtle, Screen
import random

# turtle = Turtle()
screen = Screen()

# def move_forwards():
#     turtle.forward(10)
#
# def move_backwards():
#     turtle.backward(10)
#
# def turn_left():
#     turtle.setheading(turtle.heading()+10)
#
# def turn_right():
#     turtle.setheading(turtle.heading()-10)
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()

screen.listen()
# screen.onkey(key="Up", fun=move_forwards)
# screen.onkey(key="Down", fun=move_backwards)
# screen.onkey(key="Left", fun=turn_left)
# screen.onkey(key="Right", fun=turn_right)
# screen.onkey(key="c", fun=clear)

all_turtles = []
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Make your bet man")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, y_positions[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(len(all_turtles)):
        if all_turtles[i].xcor() > 230:
            winning_turtle = all_turtles[i].pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
            is_race_on = False
            break
        rand_distance = random.randint(0,10)
        all_turtles[i].forward(rand_distance)


screen.exitonclick()