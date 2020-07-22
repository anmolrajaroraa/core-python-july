import turtle
screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(2)
#pen.shape('turtle')
pen.speed(1)
'''
pen.begin_poly()
pen.fd(100)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(100)
pen.left(90)
pen.end_poly()
p = pen.get_poly()
turtle.register_shape("Square", p)
pen.shape("Square")

pen.forward(200)
'''


print("""
    1. Circle
    2. Octagon
    3. Dot
    4. Square
    5. Rectangle
    6. Pentagon
    7. Hexagon
    8. Triangle
    9. Exit
""")

while True:   
    pen.fillcolor('darkblue')
    pen.begin_fill()
    user_input = int(input("Enter shape number to draw:"))
    if user_input == 1:
        pen.circle(100)
    elif user_input == 2:
        for i in range(8):
            pen.fd(100)
            pen.left(45)
    elif user_input == 3:
        pen.dot(200)
    elif user_input == 4:
        for i in range(4):
            pen.forward(200)
            pen.left(90)
    elif user_input == 5:
        for i in range(2):
            pen.forward(200)
            pen.left(90)
            pen.forward(100)
            pen.left(90)
    elif user_input == 8:
        for i in range(3):
            pen.forward(200)
            pen.left(120)
    elif user_input == 7:
        for i in range(6):
            pen.forward(150)
            pen.left(60)
    elif user_input == 6:
        for i in range(5):
            pen.forward(200)
            pen.left(72)
    elif user_input == 9:
        break   # terminate the loop just above me
    else:
        print("Shape doesn't exist")

    pen.end_fill()        
