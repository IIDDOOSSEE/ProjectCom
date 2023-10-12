def compare_2(x,y):
    if x > y:
        return x 
    else :
        return y 
def compare_3(x,y,z):
    a = compare_2(x,y)
    b = compare_2(a,z)
    return b 
    

max = compare_3(1,-5,8)
print("maximum is :",max)
print("max is",compare_3(2,4,-3))