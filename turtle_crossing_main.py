from turtle import Screen
import time
from turtle_crossing_player import Player
from turtle_crossing_manager import CarManager
from turtle_crossing_scoreboard import Scoreboard

# Create a turtle player that starts at the bottom of the screen and listen for the "Up"
# keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Down", fun=player.down)
screen.onkey(key="Right", fun=player.right)
screen.onkey(key="Left", fun=player.left)

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.06/cars.speed_factor)
    screen.update()

    cars.move()
    if count % 5 == 0:
        cars.create_car()

    if player.ycor() > 280:
        player.refresh()
        cars.increase_speed()
        scoreboard.increase_score()

    for car in cars.all_cars[1:]:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    count += 1

screen.exitonclick()