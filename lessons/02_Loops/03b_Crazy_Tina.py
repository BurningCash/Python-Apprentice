""""""



import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = [ ... ]
lefts = [ ... ]
colors = [  ... ]

for  i in range(8):

    forward = ...
    left = ...
    color = ...


    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  

