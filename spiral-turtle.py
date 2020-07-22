import turtle

screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(2)
pen.speed(0)

for i in range(10,35):
    pen.circle(3 * i)
    pen.left(10)
    pen.forward(10)
