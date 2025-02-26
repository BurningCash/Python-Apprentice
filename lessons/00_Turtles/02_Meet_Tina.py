import turtle
tina = turtle.Turtle()
tina = turtle.Turtle()

import random





for i in range(5):
    y = random.randint(-200, 200)
    x = random.randint(-200, 200)
    


    tina = turtle.Turtle()
    tina.right(90)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.right(90)
    tina.forward(-50)
    tina.goto(0, 50)
    tina.right(90)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.right(90)
    tina.forward(-50)
    tina.left(25)

    tina.forward(12.5)
    tina.left(25)
    tina.forward(25)
            
    tina.right(100)
    tina.forward(17.5)
    tina.right(-16)
    tina.forward(21)
    tina.penup()
    tina.goto(x, y)
    tina.pendown()








speed=(2)





turtle.exitonclick()