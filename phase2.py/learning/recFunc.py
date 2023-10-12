# 1-10 by not loop
# def num(number):
#     if number == 11:
#         return
#     print(number)
#     number+=1
#     num(number)
# num(1)

# plus number 1+2+3+4+... by not loop
# def num(number):
#     if number == 1 :
#         return number
#     else:
#         return number + num(number-1) 
# x = num(5)
# print(x)

# def fibonacci(number):
#     if number <= 1 :
#         return number
#     else:
#         return fibonacci(number-2) + fibonacci(number-1)
# for i in range(5):
#     print(fibonacci(i))

   
# 0,1,1,2,3,5,8,13
# def fibo(num):
#     a,b = 0,1 
#     while a < num :
#         print(a) 
#         a,b = b,b+a  
# fibo(10)


def fibo():
    start = [0,1]
    for i in range(10):
        start.append(start[i]+start[i+1])
    print(start)
fibo()

