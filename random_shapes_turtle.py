import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(2)
#pen.shape('turtle')
pen.speed(0)

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'brown', 'violet', 'magenta', 'purple', 'navy', 'blue',
          'chocolate', 'gray', 'white', 'pink', 'green', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'darkgreen',
          'silver', 'indigo']

for i in range(50):
    shape = random.randint(1,8)
    border_color = random.choice(colors)
    shape_color = random.choice(colors)
    x = random.randint(-250, 200)
    y = random.randint(-250, 200)
    print(x,y)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

    pen.color( border_color )
    #pen.fillcolor('#ffff00')
    pen.fillcolor( shape_color )
    pen.begin_fill()
    if shape == 1:
        pen.circle(100)
    elif shape == 2:
        for i in range(8):
            pen.fd(100)
            pen.left(45)
    elif shape == 3:
        pen.dot(200)
    elif shape == 4:
        for i in range(4):
            pen.forward(150)
            pen.left(90)
    elif shape == 5:
        for i in range(2):
            pen.forward(150)
            pen.left(90)
            pen.forward(100)
            pen.left(90)
    elif shape == 8:
        for i in range(3):
            pen.forward(150)
            pen.left(120)
    elif shape == 7:
        for i in range(6):
            pen.forward(120)
            pen.left(60)
    elif shape == 6:
        for i in range(5):
            pen.forward(120)
            pen.left(72)

    pen.end_fill()
