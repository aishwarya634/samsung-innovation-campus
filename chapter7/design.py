# make a geometric rainbow pattern
import turtle

colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor('black')

aiden = turtle.Turtle()
aiden.speed(0)

# make 36 hexagons, each 10 degrees apart
for i in range(36):

    # make hexagon by repeating 6 times
    for j in range(6):
        aiden.color(colors[i])
        aiden.forward(100)
        aiden.left(60)

    # add a turn before the next hexagon
    aiden.right(10)

# get ready to draw 36 circles
aiden.penup()
aiden.color('white')

# repeat 36 times to match the 36 hexagons
for i in range(36):
    aiden.forward(220)
    aiden.pendown()
    aiden.circle(5)
    aiden.penup()
    aiden.backward(220)
    aiden.right(10)

# hide turtle to finish the drawing
aiden.hideturtle()

turtle.done()