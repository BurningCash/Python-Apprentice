




import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina


# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location


tina.circle(5)
tina.circle(10)
tina.circle(15)
tina.circle(20)
tina.circle(25)
tina.circle(30)
tina.circle(35)
tina.circle(40)
tina.circle(45)
tina.circle(50)
tina.circle(55)
tina.circle(60)
tina.circle(65)
tina.circle(70)
tina.circle(75)
tina.circle(80)
tina.circle(85)
tina.circle(90)
tina.circle(95)
tina.circle(100)
tina.circle(105)
tina.circle(110)
tina.circle(115)
tina.circle(120)
tina.circle(125)
tina.circle(130)
tina.circle(135)

sides = (67589)
angle = sides/360


for i in range(sides):
    tina.forward(150)
    tina.left(angle)

turtle.exitonclickdone()

