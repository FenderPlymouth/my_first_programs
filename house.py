import turtle as trtl
import random

black = "#000000"
brick = "#680C07"
cream = "#F6E8B1"
brown = "#A67A5B"
trunk = "#331800"
green = "#0B6623"
bgrey = "#CFDBE6"
red = "#900D09"

painter = trtl.Turtle()
painter.speed(0)

# draw the ground
painter.penup()
painter.goto(-300, 0)
painter.pendown()
painter.goto(300, 0)

# draw tree 1
painter.penup()
painter.goto(-200, 0)
painter.color(black, trunk)
painter.begin_fill()
painter.pendown()
painter.goto(-200, 25)
painter.goto(-160, 25)
painter.goto(-160, 0)
painter.goto(-200, 0)
painter.end_fill()
painter.penup()
painter.goto(-250, 25)
painter.color(black, green)
painter.begin_fill()
painter.pendown()
painter.goto(-180, 180)
painter.goto(-110, 25)
painter.goto(-250, 25)
painter.end_fill()

# draw tree 2
painter.penup()
painter.goto(200, 0)
painter.color(black, trunk)
painter.begin_fill()
painter.pendown()
painter.goto(200, 25)
painter.goto(160, 25)
painter.goto(160, 0)
painter.goto(200, 0)
painter.end_fill()
painter.penup()
painter.goto(250, 25)
painter.color(black, green)
painter.begin_fill()
painter.pendown()
painter.goto(180, 180)
painter.goto(110, 25)
painter.goto(250, 25)
painter.end_fill()

# draw the base of the house
painter.penup()
painter.goto(-75, 0)
painter.color(black, cream)
painter.begin_fill()
painter.pendown()
painter.goto(-75, 100)
painter.goto(75, 100)
painter.goto(75, 0)
painter.end_fill()

# draw the roof
painter.penup()
painter.goto(-75, 100)
painter.color(black, brown)
painter.begin_fill()
painter.pendown()
painter.goto(0, 175)
painter.goto(75, 100)
painter.goto(-75, 100)
painter.end_fill()

# draw the door
painter.penup()
painter.goto(-55, 0)
painter.color(black, red)
painter.begin_fill()
painter.pensize(2)
painter.pendown()
painter.goto(-55, 75)
painter.goto(-5, 75)
painter.goto(-5, 0)
painter.goto(-55, 0)
painter.end_fill()
painter.penup()
painter.goto(-10, 37)
painter.color(black, black)
painter.begin_fill()
painter.circle(3)
painter.end_fill()
painter.pensize(1)

# draw the window
painter.penup()
painter.goto(15, 25)
painter.color(black, bgrey)
painter.begin_fill()
painter.pensize(2)
painter.pendown()
painter.goto(15, 75)
painter.goto(65, 75)
painter.goto(65, 25)
painter.goto(15, 25)
painter.end_fill()
painter.penup()
painter.goto(40, 25)
painter.pendown()
painter.goto(40, 75)
painter.penup()
painter.goto(65, 50)
painter.pendown()
painter.goto(15, 50)
painter.pensize(1)

# draw the chimney
painter.penup()
painter.goto(-75, 100)
painter.color(black, brick)
painter.begin_fill()
painter.pendown()
painter.goto(-75, 150)
painter.goto(-40, 150)
painter.goto(-40, 135)
painter.goto(-75, 100)
painter.end_fill()

# draw smoke from chimney
painter.penup()
painter.goto(-42, 150)
painter.setheading(90)
painter.color(black, black)
painter.begin_fill()
painter.circle(15.5, 180)
painter.end_fill()
painter.begin_fill()
painter.setheading(0)

x = -52
y = 155
r = random.randint(12, 14)
painter.goto(x, y)
painter.circle(r)
painter.end_fill()

while x >= -100:
    if r > 10:
        r = random.randint(10, (r+1))
        x += random.randint(-12, 2)
        y += random.randint(6, 12)
    elif r <= 10 and r > 5:
        r = random.randint(5, r)
        x += random.randint(-8, 1)
        y += random.randint(4, 8)
    else:
        while r > 0:
            r -= 1
            x -= 3
            y += 3
        break
    painter.begin_fill()
    painter.goto(x, y)
    painter.circle(r)
    painter.end_fill()

# hide the turtle at the end of the program
painter.hideturtle()

# create the turtle window and close it when the window is clicked
window = trtl.Screen()
window.exitonclick()
