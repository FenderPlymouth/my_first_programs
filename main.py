import turtle as trtl

painter = trtl.Turtle()

r = input("What is the radius of your curcle? ")
painter.circle(r)

window = trtl.Screen()
window.exitonclick()
