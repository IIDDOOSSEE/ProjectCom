"""
n,a,b,c  => จำนวนจาน,จานa,จานb,จานc

"""
# def hanoi(n,a,b,c):
#     if n == 0 :
#         return
#     hanoi(n-1,a,c,b) # จำนวนจาน,ย้าย,พัก,ไป
#     print("จานที่",n,"ย้ายจาก",a,"ไป",c)
#     hanoi(n-1,b,a,c)
# hanoi(3,"A","B","C")

x = int(input("ระบุแม่สูตรคูณ : "))
y = 13
def table(a,b):
    if a > 12 or a < 2 :
        print("error")
    for j in range(1,13):
        print(a,"x",j,"=",a*j)
            
table(x,y)