def check(message):
    big = 0
    small = 0 
    for item in message:
        if item.isupper():
            big+=1
        else : 
            small+=1
    return big,small
x,y = check(input("input word :"))
print("count big = ",x,"count small = ",y)
