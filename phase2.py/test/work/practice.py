# text ="            python css javascripts            "
# stript = text.strip()
# print("stript = ",stript)
# dose = "dose"
# print("split",dose.split("s"))
# print("start",dose.startswith("o"))

# import math
# import turtle
# import random
# wn = turtle.Screen()
# wn.setworldcoordinates(-1500,-500,1500,500)
# pat = turtle.Turtle()
# color = ["red","green","blue"]
# pat.pensize(5)
# def sin_curve(tur,amp):
#     for x in range(361):
#         tur_color = random.choice(color)
#         tur.color(tur_color)
#         y = amp*math.sin(math.radians(x))
#         tur.goto(x,y)
#         tur.stamp()
# sin_curve(pat,200)
# wn.exitonclick()

# data = {
#     "dose":8
# }
# print(isinstance(data,dict))

# import turtle
# import random
# wn = turtle.Screen()
# wn.bgcolor("pink")
# dose = turtle.Turtle()
# dose.shape("turtle")
# dose.color("red")
# pat = turtle.Turtle()
# pat.shape("turtle")
# pat.color("blue")
# disdose = random.randrange(250)
# dispat = random.randrange(250)
# # dose.speed(1)
# # pat.speed(1)
# print(disdose,dispat)
# def race():
#     dose.penup()
#     dose.goto(100,10)
#     dose.forward(disdose)
#     pat.penup()
#     pat.goto(100,-10)
#     pat.forward(dispat)
# race()
# wn.exitonclick()
    
# import heapq as hq
# num = [1,2,3,4,5,6]
# large = hq.nlargest(3,num)
# print(large)

# collect = ""
# text = input("input :")
# if len(text)>=2:
#     collect = collect+text[0:2]
#     collect = collect+text[-2:]
#     print(collect)
# else:
#     print("Empty String")
   
# def minimum(*args):
#   for i in args:
#     is_min = True
#     for j in args:
#       if i > j:
#         is_min = False
#         continue
#     if is_min:
#       return i
# print(minimum(5, 4, 2, 3, 2, 11, 6, 7, 9, 14, 3))

# def check(*num):
#     for i in num :
#         min = True
#         for j in num:
#             if i > j :
#                 min = False
#                 continue
#         if min :
#             return i 
# print(check(1,-5,-5,3))

# import turtle
# pat = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("black")
# pat.color("yellow")
# for i in range(5):
#     pat.forward(150)
#     pat.left(216)

# import math 
# x = math.pi
# print(x)
# print("{:.3f}".format(x))

# a = [1,2,3,4,50]
# a.remove(2)
# a.pop(1)
# print(a)


