# try :
#     num1 = int(input("num1 : "))
#     num2 = int(input("num2 : "))
#     num1 / num2 
# except ValueError :
#     print("input integer only")
# except ZeroDivisionError : 
#     print("you can't division by zero")
# except TypeError : 
#     print("input same type")

# fout = open("demo.txt","a")
# fout.write("i jame ouan")
# fout.close()    
# fout = open("demo.txt","r")
# print(fout.readline(),'\n')


# x = [5,2,1,8]
# print(sorted(x))




# food = {"pizza":40,"kfc":50,"rice":22}
# price = 0

# while True :
#     order = input("input order :")
#     if order == "0":
#         break
#     if order not in food :
#         print("order again ")
#         continue
#     for i,j in food.items():
#         if i == order:
#             price+=j
# print(price)

# star = int(input("level : "))
# for i in range(1,star+1):
#     print("*"*i)

# romandic = {
#             1:"I",
#             4:'IV',
#             5:"V",
#             9:"IX",
#             10:"x",
#             40:"XL",
#             50:"L",
#             90:"XD",
#             100:"C",
#             400:"CD",
#             500:"D",
#             900:"CM",
#             1000:"M",
#                     }
# key_roman = []
# value_roman = []
# for i in romandic.keys():
#     key_roman.append(i)
# for i in romandic.values():
#     value_roman.append(i)
# key_roman = key_roman[::-1]
# value_roman = value_roman[::-1]
# class Integer_To_Roman:
#     def __init__(self,num):
#         self.n=num
#     def change(self):
#         ans=""
#         start = 0
#         while self.n >0:
#             for i in range(self.n//key_roman[start]):
#                 ans += value_roman[start]
#                 self.n -= key_roman[start]
#             start += 1
#         return ans
# num = int(input("Enter an integer:\n"))
# changeint = Integer_To_Roman(num)
# print(f"The Roman numeral representation of {num} is {changeint.change()}")

import numpy as np
x = np.full((3,5),3.14)
print(x)
