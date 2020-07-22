import turtle
screen = turtle.Screen()
screen.bgcolor('black')
pen = turtle.Pen()
pen.color('yellow')
pen.width(3)
pen.turtlesize(2)
pen.shape('turtle')
pen.speed(10)

# for(int i = 0; i < 3; i++){
#        for(int j = 0; j < 5; j++){
#               print("%d",i);
#       }
# }

#only 1 argument -> range(stop)
#2 arguments -> range(start, stop)
#3 arguments -> range(start, stop, step)
'''for i in range(10,300,5):
    print(i)'''

'''
for i in range(30):
    #print(15*i)
    pen.forward(15*i)
    pen.left(120)
'''

'''
pen.fillcolor('darkblue')
pen.begin_fill()
for i in range(1):
   for j in range(4):
        pen.forward(300)
        pen.left(90)

pen.end_fill()'''
'''
for i in range(50): pen.circle(5 * i)
'''

#for i in range(10):
while True:   # infinite loop
    pen.fillcolor('darkblue')
    pen.begin_fill()
    user_input = input("Enter shape name:")
    if user_input == "circle":
        pen.circle(100)
    elif user_input == "square":
        for i in range(4):
            pen.forward(200)
            pen.left(90)
    elif user_input == "triangle":
        for i in range(3):
            pen.forward(200)
            pen.left(120)
    elif user_input == "hexagon":
        for i in range(6):
            pen.forward(150)
            pen.left(60)
    elif user_input == "pentagon":
        for i in range(5):
            pen.forward(200)
            pen.left(72)
    else:
        print("Shape doesn't exist")

    pen.end_fill()        
   
