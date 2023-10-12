import random
fruit = ["strawberry","apple","orange","avocado"]
word = random.choice(fruit)
word_len = len(word)
word_guess = ["_"]*word_len
change = 7
print(" ".join(word_guess))
while change > 0 and "_" in word_guess:
    guess = input("guess alphabet :")
    if len(guess) != 1 or not guess.isalpha():
        print("invalid input please input one alphabet :")
        continue
    elif guess in word :
        for i in range(len(word)) :
            if word[i] == guess:
                word_guess[i] = guess
        # print(" ".join(word_guess))
        word_guess = " ".join(word_guess)
        print(word_guess)
    else : 
        change-=1
        print(f"incorrect your change is {change}")
if "_" not in word_guess :
    print("you guess correct word Congreturation !!!")
else : 
    print("your change was out try again next time ^-^")

# mylist = [1,2,3,4,5]
# powlist = [item**2 for item in mylist]
# print(powlist)

# words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
# for item in words :
#     if item[-1] == "e":
#         item+= "d"
#     else : 
#         item+= "ed"
# print(words)