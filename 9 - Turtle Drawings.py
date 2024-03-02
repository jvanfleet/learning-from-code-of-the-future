# Let's draw some cool drawings with the package turtle

import turtle

# Let's get a nice setup in turtle
turtle.bgcolor("black") # Background color
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)

# Draw a square (NOTE - turtle always begins in the center of the screen
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.done() #allows turtle to stay on the screen

# Nice little project in turtle - creates a nice graph
# for colors in["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colors)
#     turtle.circle(150)
#     turtle.left(10)
# turtle.done()

# Let's make it cooler
for i in range(6):
    for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(10)
turtle.done()

