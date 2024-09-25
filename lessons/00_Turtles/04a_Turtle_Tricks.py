"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward(50) and tina.left(50) to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor(Gold)

tina.forward(50)
tina.pencolor(blue)
tina.left(50)
tina.pencolor(Silver)
tina.forward(50)
tina.pencolor(Teal)
tina.left(50)
turtle.exitonclick()                    # Close the window when we click on it
 