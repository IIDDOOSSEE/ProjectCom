def Sum_Avg(number):
    print(number)
    total,avg = 0,0
    for i in range(len(x)):
        total+=x[i]
    avg = total/len(x)
    return total,avg

    
x = [1,2,3,4,5,6,7,8,9,10]
y,z = Sum_Avg(x)
print("total = ",x,"average = ",y)