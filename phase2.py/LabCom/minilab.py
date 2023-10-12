# def seq3np1(n):
#     sum = 0
#     lis=[]
#     while n != 1:
#         if n % 2 == 0:        # n is even
#             n = n // 2
#         else:                 # n is odd
#             n = n * 3 + 1
#         sum+=1
#     return sum
   
# maxsofar = 0
# for i in range(1,51):
#     x = seq3np1(i)
#     if x > maxsofar :
#         maxsofar = x
#     print(x)
# print("maximum is :",maxsofar)
    # print(n)                  # the last print is 1

# seq3np1(3)


def sqrt_n_times(x,n):
    ans = x**(1/2**n)
    return ans
print(sqrt_n_times(10**8,3))
    
def cube_root(y):
    a = sqrt_n_times(y,2)**(1+1/2**2)*(1+1/2**4)*(1+1/2**8)*(1+1/2**16)*(1+1/2**32)
    return a
print(round(cube_root(27),4))



