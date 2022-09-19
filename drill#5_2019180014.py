import turtle

def reset():
    turtle.reset()
def forward():
    turtle.forward(50)
    turtle.stamp()

def left():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()
def right():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()
def backward():
    turtle.left(180)
    turtle.forward(50)
    turtle.stamp()

turtle.shape('turtle')
turtle.onkey(forward,'w')
turtle.onkey(left,'a')
turtle.onkey(right,'d')
turtle.onkey(backward,'s')
turtle.onkey(reset,'Escape')
turtle.listen()
