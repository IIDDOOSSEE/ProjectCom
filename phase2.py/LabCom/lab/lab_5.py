# 1
# for i in range(1,11):
#     if i%2==0:
#         print(i)
#     else:
#         continue
    




# 2
# print("Enter a positive integer:")
# a = int(input(""))
# summation = 0
# for i in  range(1,a):
#     if i%3 == 0 or i%5== 0:
#         summation+=i
#     else:
#         continue
# print("Sum of multiples of 3 and 5 below",a,"is:",summation)






# 3
# i=0
# while i <=15:
#     i+=1
#     if i % 3 == 0 :
#         break
#     print(i)



# 4
# def count_even_numbers(number):
#     sum = 0
#     for i in number:
#         if i %2==0:
#             sum+=1
#         else:
#             pass
#     return sum
# print(count_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(count_even_numbers([12, 15, 18, 21, 24, 27, 30])) 




# 5
# b  = []
# def is_prime(a):
#     for i in range(1,a+1):
#         if a%i == 0 :
#             b.append(i)
#     if len(b)==2:
#         return True
#     else : 
#         return False
# print(is_prime(7))  
# print(is_prime(12))  
    




# 6
# print("Enter a positive integer:")
# row = int(input())
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()




# 7
# print("Enter the number of elements:")
# a = int(input(""))
# summation = 0
# for i in range(a):
#     print("Enter a number:")
#     b = int(input(""))
#     summation+=b
# avg = summation / a 
# print("Average:",avg)





# 8
# import random
# answer = 7
# for i in range(25):
#     guess = int(input(""))
#     print("Guess the number (between 1 and 20):")
#     if guess == answer :
#         print("Congratulations! You guessed the correct number.")
#         break
#     elif guess < answer :
#         print("Too low. Try again.")
#     elif guess > answer :
#         print("Too high. Try again.")
        




# 9
# password = 'cprefamily'
# while True :
#     print("Enter the password:")
#     guess = input("")
#     if guess == password:
#         print("Access granted!")
#         break
#     else:
#         print("Incorrect password. Try again.")
    




# 10
# number = ["0","1","2","3","4","5","6","7","8","9"]
# small= "abcdefghijklmnopqrstuvwxyz"
# big = small.upper()
# count_string = 0
# count_num = 0

# print("Input a string:")
# dose = input("")
# for i in dose:
#     if i in number:
#         count_num+=1
#     elif  i in big or i in small:
#         count_string+=1
#     else:
#         continue
# print("Letters",count_string)
# print("Digits",count_num)

    







# 11
# print("Enter a string:")
# message = input("")
# vowels = ("aeiou")
# vowelsB = vowels.upper()
# count = 0
# for i in message :
#     if i in vowels or i in vowelsB:
#         count+=1
#     else:
#         continue
# print("Number of vowels:",count)





# 12
# level = int(input("level of pyramid :"))
# for i in range(1,level+1):
#     print("*"*i,end="")
#     print()




# 13




# 14





