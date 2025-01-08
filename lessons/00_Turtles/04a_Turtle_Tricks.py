import turtle
tina = turtle.Turtle()
tina.speed(0)
sides = (67589)
angle = sides/360


for i in range(sides):
    tina.forward(150)
    tina.left(angle)
    
tina.speed(0)

turtle.exitonclick()






