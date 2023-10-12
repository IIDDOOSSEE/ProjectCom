# x = float(input("input num1 : "))
# y = float(input("input num2 : "))
# print("Addition :",round(x+y,2))
# print("Addition :",round(x-y,2))
# print("Addition :",round(x*y,2))
# print("Addition :",round(x/y,2))


# x = float(input("Enter the first number:"))
# y = float(input("Enter the second number:"))
# z = float(input("Enter the third number:"))
# print("Enter the first number:")
# print("Enter the second number:")
# print("Enter the third number:")
# lis = []
# lis.append(x)
# lis.append(y)
# lis.append(z)
# print("Average:",(x+y+z)/3)
# print("Maximum:",max(lis))
# print("Minimum:",min(lis))


# print("Enter a number:")
# x = int(input(""))
# if x % 2 == 0:
#     print("Event")
# else :
#     print("Odd")

# Not complete
# Marked out of 1.00
# Flag question
# Question textWrite a program that takes the marks of a student as input and calculates their grade based on the following criteria
# Marks greater than or equal to 90: Grade A
# Marks between 80 and 89: Grade B
# Marks between 70 and 79: Grade C
# Marks between 60 and 69: Grade D
# Marks less than 60: Grade F


# print("Enter the marks:")
# grade = int(input(""))
# if grade>=90:
#     print("Grade: A")
# elif grade>=80 and grade<90:
#     print("Grade: B")
# elif grade>=70 and grade<80:
#     print("Grade: C")
# elif grade>=60 and grade<70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# x = int(input())
# if x<37:
#     print("XS")
# elif 41>x>=37:
#     print("S")    
# elif 43>x>=41:
#     print("M")    
# elif 46>x>=43:
#     print("L") 
# else :
#     print("XL")   

# x= int(input(""))
# print("Enter a year)
# if x % 4 ==0 :
#     print("",x,"is a leap year.")
# else:
#     print("",x,"is not a leap year.")


# print("Enter length of side 1:")
# print("Enter length of side 2:")
# print("Enter length of side 3:")
# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# if a == b and b == c and a == c:
#     print("Triangle type: Equilateral")
# elif a==b or a==c or b==c :
#     print("Triangle type: Isosceles")
# elif a!=b and a!=c and b!=c:
#     print("Triangle type: Scalene")


# print("Enter first number:")
# print("Enter operator (+, -, *, /):")
# print("Enter second number:")
# lis = ["+","-","*","/"]
# a = float(input(""))
# b = input("")
# c = float(input(""))
# if b in lis:
#    if b == "+":
#       print("Result:",a+c)
#    elif b == "-":
#       print("Result:",a-c)
#    elif b == "*":
#       print("Result:",a*c)
#    elif b == "/":
#       if a == 0 or c == 0:
#          print("Result: number should not be zero")  
#       else:
#          print("Result:",a/c)     
# elif b not in lis :
#    print("Result: Invalid operator")


# print("Enter the first number:")
# print("Enter the second number:")
# print("Enter the third number:")
# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# if a < 0 or b < 0 or c < 0:
#     print("Invalid input")
# elif a<=b<=c or c<=b<=a:
#     print("The median is:",b)
# elif b<=c<=a or a<=c<=b:
#     print("The median is:",c)
# elif c<=a<=b or b<=a<=c:
#     print("The median is:",a)


# x,y,z = [int(e) for e in input("").split()]
# a,b,c = [int(e) for e in input("").split()]
# import math
# distance = math.sqrt((x-a)**2+(y-b)**2)
# if distance == z+c:
#     print("touch")
# if z+c > distance:
#     print("overlap")
# if z+c < distance:
#     print("free")

# e= [int(e) for e in input("input").split()]
# print(e)
# e= [int(e) for e in range(5)]
# print(e)
