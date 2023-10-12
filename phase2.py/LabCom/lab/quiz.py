# 1
# a = int(input())
# b = int(input())
# x,y = b,a
# print(x,y)

# 2.
# import math
# print("Enter the length of side a:")
# print("Enter the length of side b:")
# print("Enter the length of side c:")
# a=float(input())
# b=float(input())
# c=float(input())
# s = (a+b+c)/2
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("Area of the triangle is:","",area)

# 3
# a = input()
# b = input()
# c = int(input())
# print((a+b)*c)

# 4
# print("Enter the first number:")
# print("Enter the second number:")
# x = float(input())
# y = float(input())
# if x > y :
#     print("The larger number is:",x)
# elif y > x :
#     print("The larger number is:",y)
# else:
#     print("The two numbers are equal.")

# 5
# print("Enter a number from 1-7:")
# a = int(input())
# if a == 1:
#     print("Sunday")
# elif a== 2 :
#     print("Monday")
# elif a== 3 :
#     print("Tuesday")
# elif a== 4 :
#     print("Wednesday")
# elif a== 5 :
#     print("Thursday")
# elif a== 6 :
#     print("Friday")
# elif a== 7 :
#     print("Saturday")
# else:
#     print("Invalid day")

# 6
# print("Enter a number:")
# a = int(input())
# if a %3 == 0:
#     print("The number is divisible.")
# else:
#     print("The number is not divisible.")

# 7
# import math
# x = float(input())
# y = (2-x)+((3/7)*x**2)-((5/11)*x**3)+math.log(x,10)
# print("{:.15f}".format(y))

# 8
# import math
# x = int(input())
# # s = math.ceil((64**(1/3)))
# # print(s)
# a = x**(1/3) 
# y= math.ceil(a)
# if (int(y))**3 == x  and type(y)==int :
#     print(y)
# else :
#     print("Not Found")

# 9
# a = input()
# b = ord(a)
# print(b)

# 10
# text = input()
# reverse = int(text[::-1])

# print("Enter a number: Reversed number:",reverse)

# 11
# a = input()
# b = input()
# if b in a :
#     x = a.count(b)
# print("Enter a string: Enter a character:","The number of occurrences:",x)




# 12
# import random
# a = ["Heads","Tails"]
# for seed_value in range(1, 11):
#     random.seed(seed_value)
#     x = random.choice(a)
#     print("Seed:",str(seed_value)+""+",","Coin Flip:",x)

# 13
# import math
# def  calculate_factorial():
#     print("give me a number:")
#     a = input()
#     for item in a :
#         if item.isalpha():
#             print("please insert number")
#             break
#         else:
#             a = int(a)
#             b = math.factorial(a)
#             print(b)
#             break
# calculate_factorial()

# 14
# print("Enter a number:")
# a = int(input("")) 
# def is_prime_simple():
#     lis = []
#     for i in range(1,a+1):
#         if a % i ==0:
#             lis.append(i)
#     if len(lis) ==2:
#         print(a,"is a prime number.")
#     else : 
#         print(a,"is not a prime number.")
# is_prime_simple()

# 15    
# print("Enter an email address:")
# email = input()
# if (email[0] =="s" or email[0]=="S" and email[1:14].isdigit()) and ("@email.kmutnb.ac.th" in email and  email[3:9] =="010126"):
#     print("The email belongs to email.kmutnb.ac.th")
#     print("Greeting! Cpr.E student")
# elif (email[0] =="s" or email[0]=="S") and (email[1:14].isdigit() and "@email.kmutnb.ac.th" in email):
#     print("The email belongs to email.kmutnb.ac.th")
# else :
#     print("Invalid email")



# 16
# for i in range(100,201):
#     if i%5 ==0 and i%7==0:
#         print(i)
#         break

# 17
# level = 5
# count = 1
# for i in range(1,level+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#     count+=1
#     print()

# 18
# print("Enter a positive integer:")
# level = int(input())
# for i in range(level,0,-1):
#     print("*"*i)
    
# 19
# print("Enter a password:")
# guess = input()
# def is_valid_password(password):
#     return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
# while True:
#     if is_valid_password(guess) == True:
#         print("Password is valid.")
#         break
#     else:
#         print("Invalid password try again.")
#         print("Enter a password:")
#         guess = input()

# 20
# print("Enter the word(s) to wrap:")
# print("Enter the HTML tag to use:")
# a = input()
# b = input()
# print("HTML string:","<"+b+">"+a+"</"+b+">")

# 21
# char = 0
# digit = 0
# symbol = 0
# print("Enter a string:")
# text = input()
# for i in text:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         symbol+=1
# print("Total counts of characters, digits, and symbols:")
# print("Chars =",char,"Digits =",digit,"Symbols =",symbol)

# 22

# 22
# word = "python"
# lenght_word = len(word)
# guess_word = ["_"] * lenght_word
# attempt = 5
# while attempt > 0 and "_"  in guess_word:
#     guess = input('guess letter : ')
#     if len(guess) != 1 or not guess.isalpha() :
#         print("invalid input try again !")
#         continue
#     elif guess in word:
#         for i in range(len(word)):
#             if word[i] == guess:
#                 guess_word[i]= guess
#         print(" ".join(guess_word))
#     else :
#         attempt-=1
#         print("incorrect try again !","attempt = ",attempt)
    
# if  "_" not in guess_word :
#     print("congreturation")
# else :
#     print("nice try")