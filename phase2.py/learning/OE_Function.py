def Odd_Event():
    odd = []
    even = []
    while True:
        num = (input("input number :"))
        if num == "exit":
            break
        elif int(num)%2==0:
            even.append(int(num))
        elif int(num)%2!=0:
            odd.append(int(num))
    print("odd =>",odd)
    print("even =>",even)
Odd_Event()