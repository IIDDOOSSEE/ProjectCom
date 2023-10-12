# send list into function
def datafruit(fruit1,fruit2):
    print(fruit1)
    print(fruit2)
a = ["banana","watermalon"]
b = ["coconut","apple"]
datafruit(a,b)
print()
# applied
def Count_fruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ : ",i+1,"ได้แก่ : ",item[-2:i])
s = ["orange","pinespple","grape"]
Count_fruit(s)
