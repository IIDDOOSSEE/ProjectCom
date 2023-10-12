# special circle 
# import turtle
# tatar = turtle.Turtle()
# wn = turtle.Screen()
# tatar.pensize = 5
# x = tatar.pencolor = ["blue","hotpink","green"]
# # for a in  x:
# #     tatar.color = a.[0]
# for i in range(360):
#         tatar.forward(1)
#         tatar.left(1)
# wn.exitonclick()


# 1
# print("Enter the length of the rectangle:")
# print("Enter the width of the rectangle:")
# def calculate_area():
#     x = float(input())
#     y = float(input())
#     return x * y 
# print("The area of the rectangle is:",calculate_area())

# 2
# print("Enter the first number:")
# print("Enter the operator (+, -, *, /):")
# print("Enter the second number:")
# def calculator(x,y,z):
#     if y =="+":
#         return x +z 
#     elif y =="-":
#         return x-z 
#     elif y =="*":
#         return x*z 
#     elif y =="/":
#         return x/z 
#         if z==0:
#             return
#     else : 
#         return x/z
# a = float(input())
# b = input()
# c = float(input())
# print("Result:",calculator(a,b,c))

# 3
# print("Enter the first number:")
# print("Enter the second number:")
# print("Enter the third number:")    
# aa = float(input())
# bb = float(input())
# cc = float(input())
# def min_2(a,b):
#     if a>b :
#         return b 
#     else :
#         return a
# def min_3(a,b,c):
#     x = min_2(a,b)
#     y = min_2(x,c)
#     return y
# result = min_3(aa,bb,cc)  
# print("Minimum:",result)

# 4
# print("Enter a word:")
# def word():
#     word = input("")
#     return word
# print(word())
    
# 5
# def salary(name,salary= 2000):
#     print("Name:",name,"salary:",salary)
# salary("Ryu",15000)
# salary("KJ")

# 6
# print("Enter the first number:")
# print("Enter the second number:")
# a = float(input())
# b = float(input())
# def Plus_minus(c,d):
#     x = c+d,c-d
#     print(x)
# Plus_minus(a,b)

# 7
# print("Enter a year:")
# year = int(input())
# def is_leap_year(x):
#     if x % 4 ==0:
#         print("it's a leap year.")
#     else:
#         print("it's not a leap year.")
# is_leap_year(year)

# def add_numbers(*number):
#     summation = 0
#     for i in number :
#         summation += i
#     print("Sum of numbers:",summation)
# add_numbers(10, 15, 20)
# add_numbers(5, 7, 12, 3, -20, 1.345, 0, 1, 9)

# 9
# def print_date(year,month,*date):
#     print("Year:",year)
#     print("Month:",month)
#     for i in date :
#         if date == ():
#             return
#         else :
#             print("Date:",i)
    
# print_date(2023, 7)   
# print()
# print_date(2023, 7, 24) 

# 10
# x=10
# def convert():
#     global x 
#     x = 20
# print("Before function call: global_variable =",x)
# convert()
# print("After function call: global_variable =",x)

# 11
# def one():
#     print("This is the first function.")
# def two(a):
#     print("This is the second function.")
# two(one())

# 12
# a = float(input())
# b = float(input())
# print("Enter the length of the rectangle:")
# print("Enter the width of the rectangle:")
# area = lambda width,length:width*length
# print("The area of the rectangle is:",area(a,b))

# 13
# numbers_list = [1, 2, 3, 4, 5]
# def summation():
#     summation = 0
#     for i in numbers_list :
#         summation+=i
#     return summation
# print("Sum of numbers:",summation())

# 14
# numbers_list = [23, 56, 10, 35, 42, 78]
# def compare():
#     maximum = 0
#     for item in numbers_list:
#         if item>maximum:
#             maximum = item
#     print("Maximum number:",maximum)    
# compare()

# 15  
# print("Enter an integer:")
# a = int(input("")) 
# def is_prime_simple():
#     lis = []
#     for i in range(1,a+1):
#         if a % i ==0:
#             lis.append(i)
#     if len(lis) ==2:
#         print("it's the number prime.")
#     else : 
#         print("it's not the number prime.")
# is_prime_simple()

# def date(year,month,*date):
#     print("year : ",year)
#     print("month : ",month)
#     for i in date:
#         if date == ():
#             pass
#         else:
#             print("date :",i)
#     return ""
# print(date(2023,7))
# print()
# print(date(2023,7,24))
