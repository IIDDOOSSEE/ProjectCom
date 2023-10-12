# 47
# time = input("Enter time in 24-hour format (HH:MM):\n")
# hour = int(time[0:2])
# if hour > 12 :
#     hour-=12
#     print("Time is 12-hour formats:",str(hour)+time[2:],"PM")
# elif hour < 12:
#     if len(time)==5:
#         print("Time is 12-hour formats:",time[1:],"AM")
#     else :
#         print("Time is 12-hour formats:",time,"AM")

# 49
# x = input("input your ISBN :")
# summation = 0

# lis = [10,9,8,7,6,5,4,3,2]
# for i in range(9):
#     summation+=int(x[i])*lis[i]
# print(summation)
# count = 0
# while summation % 11 !=0:
#     count+=1
#     summation+=1
# print(x+str(count))    

# 50
money = 0
people = (input("people : "))
x = people
while True :
    if people == 0:
        break
    if not people.isdigit():
        print("Invalid input. Please enter invalid number")
        break
    people = int(people)
    if people >1000000 :
        break
    if people < 0 :
        print("Please enter a positive number")
        break
    if people >=13:
        room  = people // 13
        money+=room*3000
        people %= 13
    if people >=5:
        room = people//5
        money+=room*1500
        people %= 5
    if people >=2:
        room = people//2
        money+=room*800
        people %= 2
    if people >=1:
        room    = people
        money+=room*500
        break
    
print(money)
print(f"Total cost for {x} people is {money} baht")
        

# 21000+1500