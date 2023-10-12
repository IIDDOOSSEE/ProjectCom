# 12 
# import math
# x = float(input())
# y =math.log10(x**10)-(3*x**2)+(9*x)*math.fabs(x**2-2*x)+1
# print(y)

# import math
# print(math.pi)
# print(math.e)

# 14
# import math
# print("Enter the first number:")
# print("Enter the second number:")
# x = int(input())
# y = int(input())
# z = math.gcd(x,y)
# print(z)

# 15
# import random
# for seed_value in range(1, 11):
#     random.seed(seed_value)
#     x = random.randint(1,101)
#     print("Seed:",str(seed_value)+",","Random Number:",x)

# 16
# import math
# x = int(input())
# y = int(input())
# z = math.sqrt(x**2+y**2)
# print(z)

# 17
import math
print("Input coordinates of two points:")
print("Starting latitude::")
print("Starting longitude::")
print("Ending latitude:")
print("Ending longitude:")

a = float(input())
b = float(input())
c = float(input())
d = float(input())
r = 6371.01
def rad(h):
    rad = h * math.pi/180
    return rad
x = math.sin((rad(a)-rad(c))/2)**2+(math.cos(rad(a))*math.cos(rad(c))) * (math.sin((rad(b)-rad(d))/2)**2)
distance = 2*r*math.asin(math.sqrt(x))
str(distance)
print("The distance is","%.2f"%(distance)+"km.")


# 18
# x = int(input())
# for i in range(1,x+1):
#     if x % i == 0 :
#         print(i)

# 19
# import math
# n = int(input())
# for i in range(n):
#     if n < 0 :
#         break
#     x = int(input())

# 19
# lis = []
# minus = 0 
# n = int(input())
# for i in range(n):
#     if n < 0 :
#         break
#     x = int(input())
#     if x<0:
#         minus+=1
#     lis.append(x)
# max = max(lis)
# min = min(lis)
# result = max - min
# print(result,minus)
  
    
