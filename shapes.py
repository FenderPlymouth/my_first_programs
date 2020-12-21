import turtle as trtl


def draw_triangle():  # defines the equalateral triangle finction
    i = 0  # sets the counter equal to 0
    while i <= 2:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(120)  # angle = 360 / number of sides
        i += 1  # adds 1 to the counter


def draw_square():  # defines the square finction
    i = 0  # sets the counter equal to 0
    while i <= 2:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(100)  # angle = 360 / number of sides


# hexagon
# heptagon
# octogon
# nonagon
# decagon
# circle


fred = trtl.Turtle()  # defines the name of my turtle as fred
fred.shape("turtle")  # changes the painter shape from an arrow to a turtle...becasue I can...
window = trtl.Screen()

again = "Y"
while again.upper() == "Y":
    shape = trtl.textinput("Number of Sides:", "How many sides do you want to draw?")
    side = trtl.textinput("Side Length:", "How long do you want your sides?")
    side = float(side)

    if shape == "3":
        draw_triangle()
    elif shape == "4":
        draw_square()
    else:
        print("not in my programing...")

    again = trtl.textinput("New Shape:", "Draw a new shape?(Y/N")
    fred.clear()

window.done()
