import turtle as t
import random
import colorgram

t.colormode(255)


turtle = t.Turtle()
turtle.shape("arrow")
turtle.color("black")

# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# for i in range(8):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
# turtle.pendown()
# turtle.forward(10)

# colors = ["tomato", "green yellow", "blue", "red", "medium orchid", "peach puff"]
# for n in range(3,11):
#     sum_of_interior_angles = (n-2)*180
#     angle = sum_of_interior_angles/n
#     turtle.pensize(2)
#     turtle.color(random.choice(colors))
#     for i in range(n):
#         turtle.forward(100)
#         turtle.right(180-angle)

# def generate_ranodom_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0,90,180,270]
# turtle.pensize(15)
# turtle.speed("fastest")
#
# for _ in range(200):
#     direction = random.choice(directions)
#     turtle.color(generate_ranodom_color())
#     turtle.forward(30)
#     turtle.setheading(direction)

# turtle.speed("fastest")
#
# def draw_spirograph(sizeofgap):
#     for _ in range(360 // sizeofgap):
#         turtle.color(generate_ranodom_color())
#         turtle.circle(100)
#         turtle.setheading(turtle.heading()+sizeofgap)
#
# draw_spirograph(5)
#
# color_list = []
# colors = colorgram.extract('image.jpg', 100)
# for col in colors:
#     first_color = col
#     rgb = first_color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     color_list.append((red, green, blue))
#
#
# turtle.penup()
# turtle.setheading(225)
# turtle.forward(300)
# turtle.setheading(0)

# for i in range(10):
#     for j in range(10):
#         turtle.color(random.choice(color_list))
#         turtle.pendown()
#         turtle.dot(20)
#         turtle.penup()
#         turtle.forward(50)
#
#     y = turtle.position()[1]
#     turtle.home()
#     turtle.sety(y+30)

# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots+1):
#     turtle.dot(20, random.choice(color_list))
#     turtle.forward(50)
#
#     if dot_count % 10 == 0:
#         turtle.setheading(90)
#         turtle.forward(50)
#         turtle.setheading(180)
#         turtle.forward(500)
#         turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
