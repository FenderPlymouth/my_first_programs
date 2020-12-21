import turtle as trtl

rise = 0

carl = trtl.Turtle()

carl.goto(100, 0)
carl.goto(0, 300)
carl.goto(0, 0)

while rise < 300:
    carl.penup()
    carl.goto(0, rise)
    carl.pendown()
    x = (rise - 300) / (-3.5)
    y = (0.5 * x) + rise
    carl.setheading(carl.towards(x, y))
    carl.forward(((x * x) + (50 * 50)) ** 0.5)
    rise += 50


window = trtl.Screen()
window.exitonclick()
