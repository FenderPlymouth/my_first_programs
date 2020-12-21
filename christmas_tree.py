import turtle as trtl

carl = trtl.Turtle()
trunk = "brown"
tree = "dark green"
star = input("star color ")
size = input("star size ")

carl.penup()
carl.goto(-20, -100)
carl.pendown()
carl.color("black", trunk)
carl.begin_fill()
carl.goto(20, -100)
carl.goto(20, -60)
carl.goto(-20, -60)
carl.goto(-20, -100)
carl.end_fill()

carl.penup()
carl.goto(-100, -60)
carl.pendown()
carl.color("black", tree)
carl.begin_fill()
carl.goto(100, -60)
carl.goto(0, 260)
carl.goto(-100, -60)
carl.end_fill()

carl.penup()
carl.goto(0, 260)
carl.pendown()
carl.color("black", star)
carl.begin_fill()
carl.circle(int(size))
carl.end_fill()


window = trtl.Screen()
window.exitonclick()
