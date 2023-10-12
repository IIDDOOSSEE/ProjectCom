# color = {"red":"สีแดง","blue":"สีส้ม","green":"สีเขียว"}
# print(color)
# color.update({"yellow":"สีเหลือง","black":"สีดำ"})
# print(color)
# color.pop("blue")
# print(color)
# for i in color.keys():
#     print(i)
# print()
# for j in color.values():
#     print(j)
# print()
# for k,v in color.items():
#     print("key = ",k,"value = ",v)

# while True:
#     price = 0
#     menu = {"ไข่เจียว":30,"กระเพรา":45,"น้ำปั่น":15}
#     order = input("input menu :")

# color = {"red":"สีแดง","blue":"สีส้ม","green":"สีเขียว"}
# print(color.get("yellow","not a python"))
# print(list(color.keys()))

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)