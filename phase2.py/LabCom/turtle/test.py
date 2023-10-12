# import turtle
# wn = turtle.Screen()
# wn.bgcolor("pink")
# wn.screensize(canvwidth=500,canvheight=500,bg="cyan")
# ayi = turtle.Turtle()
# ayi.color("blue")
# ayi.shape("turtle")
# ayi.up()
# ayi.goto(20,100)
# ayi.stamp()
# ayi.goto(100,100)
# # ayi.forward(-100)

# wn.exitonclick()

import turtle

def draw_letter(x, y, letter):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    if letter == "I":
        pen.forward(10)
        pen.backward(5)
        pen.left(90)
        pen.forward(20)
        pen.right(90)
        pen.forward(5)
        pen.backward(10)
    elif letter == "H":
        pen.left(90)
        pen.forward(20)
        pen.backward(10)
        pen.right(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(10)
        pen.left(180)
        pen.forward(20)
        pen.right(90)
    elif letter == "A":
        pen.left(75)
        pen.forward(20)
        pen.backward(10)
        pen.right(75)
        pen.forward(10)
        pen.right(75)
        pen.forward(10)
        pen.backward(30)
        
        # pen.backward(10)
    
    # elif letter == "T":
    #     pen.left(90)
    #     pen.forward(20)
    #     pen.penup()
    #     pen.backward(10)
    #     pen.pendown()
    #     pen.left(90)
    #     pen.forward(10)
    #     pen.left(90)
    #     pen.forward(5)
    #     pen.backward(10)
    # elif letter == "E":
    #     pen.left(90)
    #     pen.forward(20)
    #     pen.right(90)
    #     pen.forward(10)
    #     pen.backward(10)
    #     pen.right(90)
    #     pen.forward(10)
    #     pen.left(90)
    #     pen.forward(10)
    #     pen.right(90)
    #     pen.forward(10)
    #     pen.backward(20)
    # elif letter == "C":
    #     pen.penup()
    #     pen.goto(x + 5, y)
    #     pen.pendown()
    #     pen.left(90)
    #     pen.circle(10, 180)

screen = turtle.Screen()
screen.title("I HATE COM")
screen.bgcolor("pink")

pen = turtle.Turtle()
pen.speed(1)

word = "I HATE COM"
x_pos = -100

for letter in word:
    draw_letter(x_pos, 0, letter)
    x_pos += 50

pen.hideturtle()
# turtle.done()
screen.exitonclick()
