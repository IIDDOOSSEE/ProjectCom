import turtle
import random
wn = turtle.Screen()
wn.bgcolor("pink")
pat = turtle.Turtle()
pat.shape("turtle")
pat.pensize(10)
color = ["blue","green","red","yellow","orange","white"]
def pentagon():
    decorate = 0
    for i in range(6):
        x = color[decorate]
        pat.forward(100)
        pat.left(60)
        pat.color(x)
        decorate +=1
# pentagon()
def sibhok():
    pat.penup()
    pat.goto(0,-200)
    pat.pendown()
    for i in range(16):
        line = random.choice(color)
        pat.forward(100)
        pat.left(360/16)
        pat.color(line)
# sibhok()

def samsibsong():
    wn.screensize(canvheight=10000,canvwidth=10000)
    pat.penup()
    pat.goto(0,-200)
    pat.pendown()
    for i in range(32):
        line = random.choice(color)
        pat.forward(50)
        pat.left(360/32)
        pat.color(line)
samsibsong()
wn.exitonclick()