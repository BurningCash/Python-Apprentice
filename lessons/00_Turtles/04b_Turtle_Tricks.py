import turtle
tina = turtle.Turtle()

sides = (7955)
angle = sides/360

tina.pentagon(50)


for i in range(sides):
    tina.forward(150)
    tina.left(angle)
    
turtle.exitonclick()
