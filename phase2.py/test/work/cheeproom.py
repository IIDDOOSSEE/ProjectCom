# # people = int(input("people : "))
# # def check(n):
    
    
x=input()
people= x
error=0
budget=0
while True:
    if str(x)[0].isalpha():
        print("Invalid input. Please enter a valid number.")
        break
    x=int(x)
    if x <=0:
        print("Please enter a positive number.")
        break
    if x>=13:
        a1=round(x/13)
        budget+=a1*3000
        x=x%13
    if x>=5:
        a2=round(x/5)
        budget+=a2*3000
        x=x%5
    if x>=2:
        a3=round(x/2)
        budget+=a3*3000
        x=x%2
    if x>=1:
        budget+=(x)*500
        break
if budget>0:
    print(f"Total cost for {people} people is {budget} baht")


# a2 = round(8/5)
# a1 = 8//5
# print(a2,a1)