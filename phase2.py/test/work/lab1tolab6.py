# 1.6
# h = int(input())
# m = int(input())
# s = int(input())
# print(3600*h+60*m+s)

#1.7
# a = int(input())
# x = 1 
# x = ( x + a/x ) /2
# x = ( x + a/x ) /2
# x = ( x + a/x ) /2
# x = ( x + a/x ) /2
# print(x)

# 1.10
# a,b,c = [ e for e in input().split()]
# print((a+b+c)+(a+b)*int(c))

# 1.11
# a,b,c,d,e = [int(x) for x in input().split()]
# print((a+b+c+d+e)/5)

# --------------------------------------------------------------------------
# lab2
# 2.1
# a = float(input("first num :"))
# b = float(input("second num :"))
# print("add :",a+b)  
# print("minus :",a-b)
# print("multiple :",a*b)
# print("division : ","{:.2f}".format(a/b))
# print("division :","%.2f"%(a/b))

# 2.2
# a = float(input("num1:"))
# b = float(input("num2:"))
# c = float(input("num3:"))
# lis = []
# lis.append(a)
# lis.append(b)
# lis.append(c)
# print("avg = ","%.3f"%((a+b+c)/3))
# print("max = ",max(lis))
# print("min = ",min(lis))
# avg = ("%.2f"%((a+b+c)/3))
# avgs = "{:.5f}".format((a+b+c)/3)
# print(type(avg))
# print(type(avgs))

# 2.15
# a = float(input("num1 : "))
# b = input("oprator : ")
# c = float(input("num2 : "))
# if b == "+":
#     print("result :",a+c)
# elif b == "-":
#     print("result :",a-c)
# elif b == "*":
#     print("result :",a*c)
# elif b == "/":
#     if c == 0:
#         print("error")
#     else:
#         print("result :",a/c)
# 2.16
# a = float(input("num1:"))
# b = float(input("num2:"))
# c = float(input("num3:"))
# if a>=b and b>=c :
#     print("median is : ",b)
# elif b>=a and a>=c :
#     print("median is : ",a)
# elif b>=c and c>=a :
#     print("median is : ",c)
# 2.17
# a,b,c = [int(e) for e in input().split()]
# d,e,f = [int(e) for e in input().split()]
# distance = ((a-d)**2 + (b-e)**2)**(1/2)
# rad = c+f 
# if distance == rad :
#     print("touch")
# elif distance > rad :
#     print("free")
# else : 
#     print("overlap")
# print(distance)
# -------------------------------------------------------------
# lab3
# 3.12
# import math
# x = int(input("num :"))
# a = math.log10(x**10)-(3*x**2)+(9*x)*abs((x**2)-(2*x))+1
# print(a)

# 3.15
# import random
# for a in range(1,11):
#     random.seed(a)
#     x = random.randint(1,101)
#     print("seed",a,"random",x)

# 3.17
# import math
# a = float(((input("start lat : "))))
# c = float(((input("start long : "))))
# b = float(((input("end lat : "))))
# d = float(((input("end long : "))))
# r = 6371.01 
# def rad(x):
#     rad = x*math.pi/180
#     return rad
# h = math.sin((rad(b)-rad(a))/2)**2+math.cos(rad(a))*math.cos(rad(b))*math.sin((rad(d)-rad(c))/2)**2
# distance = 2*r*math.asin(math.sqrt(h))
# print("%.2f"%distance)

# 3.18
# n = int(input("num :"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# 3.19
# n = int(input("many :"))
# minus = 0 
# max = 0
# lis = []
# for i in range(n):
#     a = int(input("num"))
#     lis.append(a)
#     if n<0:
#         break
#     elif a<0 :
#         minus +=1 
# print(max(lis)-min(lis),minus)


# -------------------------------------------------------------
# lab4
# 4.1
# x = float(input("widht :"))
# y = float(input("height :"))
# def calArea(a,b):
#     return a*b
# print(calArea(x,y))

# 4.2
# a = float(input("num 1 "))
# b = input("opertor")
# c = float(input("num 2 "))
# def calculator(x,y,z):
#     if y == "+":
#         return a+c 
#     elif y == "-":
#         return a-c
#     elif y == "*":
#         return a*c
#     elif y == "/":
#         if c == 0:
#             return "error"
#         else:
#             return a/c 
# print("result = ",calculator(a,b,c))

# 4.5
# a = float(input("num 1 :"))
# b = float(input("num 2 :"))
# c = float(input("num 3 :"))
# def compare_3(x,y,z):
#     if x<= y and x <= z :
#         return x 
#     elif y <=x and y <= z :
#         return y 
#     else :
#         return z 
# print("min = ",compare_3(a,b,c))

# def salary(name,salary = 2000):
#     print("name :",name,"salary : ",salary)
# salary("ryu",15000)
# salary("kj")

# 4.6
# def AddMinus(x,y):
#     return x+y,x-y
# a = float(input("num1"))
# b = float(input("num2"))
# print(AddMinus(a,b))

# 4.9
# def date(year,month,*date):
#     print("year : ",year)
#     print("month : ",month)
#     if date ==():
#         return ""
#     else : 
#         for i in date:
#             print("date:",i)
# date(21,7,10) 
# date(21,7) 

# 4.11
# def one():
#     print("first func")
# def two():
#     one()
#     print("second func")
# two()

# 4.12
# a = float(input())
# b = float(input())
# area = lambda x,y : x*y
# print(area(a,b))

# 4.14
# max = 0
# numbers_list = [23, 56, 10, 35, 42, 78]
# for i in numbers_list:
#     if i>max:
#         max = i
# print(max)

# 4.15
# lis = []
# def is_prime_simple():
#     num = int(input("num:"))
#     for i in range(1,num+1):
#         if num % i == 0 :
#             lis.append(i)
#     if len(lis) == 2:
#         print("prime number")
#     else:
#         print("not prime number")
# is_prime_simple()

# 5.1
# for i in range (1,11):
#     if i%2==0:
#         print(i)
#     else:
#         continue

# 5.2
# summation = 0
# a = int(input("num : "))
# for i in range(1,a):
#     if i%3 ==0 or i%5 ==0 :
#         summation+= i
#     else :
#         continue
# print(summation)

# 5.3
# i = 1
# while i<=15:
#     if i % 3 ==0 :
#         break
#     print(i)
#     i+=1

# 5.6
# a = int(input("level :"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# b = int(input("lv : "))
# for i in range(1,b+1):
#     print("*"*i)
# b = int(input("lv : "))
# n = b-1
# for i in range(1,b+1):
#     for j in range(n):
#         print(" ",end="")
#     n-=1
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()

# 5.7
# sum = 0
# a = int(input("count:"))
# for i in range(a):
#     b = int(input("num :"))
#     sum += b
# print("avg = ",sum/a)

# 5.8
# import random 
# random.seed(15)
# x = random.randrange(1,21)
# while True :
#     guess = int(input("guess num :"))
#     if guess == x :
#         print("correct") 
#         break
#     elif guess > x :
#         print("more")
#     elif guess < x :
#         print("less")

# 5.10
# alpha = 0
# digit = 0
# text = input("text :")
# for i in text : 
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
#     else :
#         continue
# print(alpha,digit)

# 5.11
# count = 0 
# text = input("text : ")
# vowel = "aeiouAEIOU"
# for item in text :
#     if item in vowel:
#         count+=1
# print(count)
        