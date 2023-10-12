# return  --- ส่งค่าออกมาในโปรแกรมหลัก
# def Random(a):
#     if a == 99:
#         print("ถูกหวย")
#         return 10000    
#     else :
#         print("ถูกหวย(กิน)")
#         return 0 
# b  = int(input("input number for random : "))
# debt  = 1000
# result = Random(b) - debt 
# print("เงินคงเหลือ",result)
print()
# return สามารถข้ามการทำงานได้เหมือน break 
def three_digit(a):
    if len(str(a)) !=3 :
        return
    if a == 999:
        print("ถูกหวย")
        return 10000    
    else :
        print("ถูกหวย(กิน)")
        return 0 
x = int(input("input num 3 digit : "))
three_digit(x) # ไม่เอา return
print(three_digit(x))
