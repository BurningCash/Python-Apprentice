import turtle
tina = turtle.Turtle()

sides = 6
angle =  sides

for i in range(sides):
    
    tina.left(angle)
    tina.forward(50)

turtle.exitonclick()
