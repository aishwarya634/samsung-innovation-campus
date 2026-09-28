import turtle
from datetime import datetime

# Screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Analog Clock")

# Turtle
aiden = turtle.Turtle()
aiden.speed(0)
aiden.hideturtle()

# Draw clock circle
aiden.penup()
aiden.goto(0, -200)
aiden.pendown()
aiden.circle(200)

# Draw hour marks
for i in range(12):
    aiden.penup()
    aiden.goto(0, 0)
    aiden.setheading(90 - i * 30)
    aiden.forward(180)
    aiden.pendown()
    aiden.forward(20)

# Draw numbers
for i in range(1, 13):
    angle = 90 - i * 30
    aiden.penup()
    aiden.goto(0, 0)
    aiden.setheading(angle)
    aiden.forward(155)
    aiden.write(
        str(i),
        align="center",
        font=("Arial", 16, "normal")
    )

# Get current time
now = datetime.now()

hour = now.hour % 12
minute = now.minute
second = now.second

# Function to draw a hand
def draw_hand(angle, length, width):
    hand = turtle.Turtle()
    hand.speed(0)
    hand.hideturtle()
    hand.width(width)

    hand.penup()
    hand.goto(0, 0)
    hand.setheading(angle)
    hand.pendown()
    hand.forward(length)


# Calculate angles
hour_angle = 90 - (hour * 30 + minute * 0.5)
minute_angle = 90 - (minute * 6)
second_angle = 90 - (second * 6)

# Draw hands
draw_hand(hour_angle, 100, 6)
draw_hand(minute_angle, 140, 4)
draw_hand(second_angle, 170, 2)

# Center dot
aiden.penup()
aiden.goto(0, -5)
aiden.dot(10)

turtle.done()