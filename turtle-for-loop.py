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
    print(15*i)
    pen.forward(15*i)
    pen.left(120)
'''

for i in range(10):
   for j in range(4):
        pen.forward(30 * i)
        pen.left(90)

for i in range(50): pen.circle(5 * i)
