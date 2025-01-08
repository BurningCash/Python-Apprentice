import turtle
tina = turtle.Turtle()
tina.speed(0)
sides = (67955)
angle = sides/360

tina.pentagon(50)


for i in range(sides):
    tina.forward(150)

    tina.speed(0)
    
    tina.left(angle)

    
turtle.exitonclick()
