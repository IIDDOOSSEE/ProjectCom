# 1
# print("Enter a list of characters separated by spaces:")
# a = [e for e in input().split()]
# b = ""
# for i in a :
#     b = b+i
# print("Converted string:",b)


# 2
# lis = []
# print("Enter a tuple of integers:")
# a = [int(e) for e in input().split()]
# f = len(a)
# for i in range(f):
#     i = i *a[i]
#     lis.append(i)
    
# print("Modified tuple:",tuple(lis))

# 3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lis = reversed(numbers)
# for i in lis :
#     print(i)

# 4
# print("Enter elements for list 1 (space-separated):")
# print("Enter elements for list 2 (space-separated):")
# lis1 = []
# lis2 = []
# a = [e for e in input().split()]
# g = [c for c in input().split()]
# for i in a :
#     lis1.append(i)
# for j in g :
#     lis2.append(j)
# print("List 1:",lis1)
# print("List 2:",lis2+lis1)

# 5
# print("Enter words separated by spaces:")
# a = [e for e in input().split()]
# for i in a :
#     print("Length of",i+":",len(i))

# 6
# import random
# population = ['red', 'blue', 'green', 'yellow', 'orange']
# for seed_value in range(1, 11):
#     lis = []
#     random.seed(seed_value)
#     x = random.choice(population)
#     lis.append(x)
#     print("Seed:",str(seed_value)+",","Random Sample:",lis)

# 7
# a = [e for e in input("Enter words separated by spaces:\n").split()]
# lis = []
# for i in a :
#     lis.append(i[0])
# print("First characters:",lis)

# 8
# a = [int(e) for e in input("Enter a list of numbers separated by spaces:\n").split()]
# lis = []
# for i in a :
#     if i %2 != 0:
#         lis.append(i)
#     else : 
#         continue
# print("Numbers after removing even numbers:",lis)
# print("Numbers after removing even numbers:",lis)        

# 9
# a = [e for e in input("Enter the first list of elements separated by spaces:\n").split()]
# b = [e for e in input("Enter the second list of elements separated by spaces:\n").split()]
# def compare(x,y):
#     for i in x :
#         for i in y :
#             if i in y :
#                 print("The lists have at least one common member.")
#                 break
#             else :
#                 print("The lists do not have any common members.")
#                 break
# compare(a,b)

# 10
# lis = []
# a = [e for e in input("Enter elements for the first list separated by spaces:\n").split()]
# b = [e for e in input("Enter elements for the second list separated by spaces:\n").split()]
# for i in range(len(a)):
#     x  = a[i],b[i]
#     lis.append(x)
# print("Combined list of tuples:",(lis))

# 11
import random

word = ["python", "hangman", "programming", "computer", "challenge", "learning"]
user_seed = int(input("Enter a seed for the random number generator: Welcome to Hangman!\n"))
random.seed(user_seed)
word_get = random.choice(word)
guess = []
guessed = []
for i in word_get:
    guess.append("_")
attempts = 6

def print_guess():
    text = ""
    for item in guess:
        text = text + item
    return print(text)
    
print_guess()

while attempts > 0:
    user = input("Guess a letter: ")
    if user in guessed:
        print("You already guessed that letter.")
    else:
        
        if user in word_get:
            print("Correct guess!")
            lposition = word_get.find(user)
            rposition = word_get.rfind(user)
            guess[lposition] = user
            guess[rposition] = user
            print_guess()
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            print_guess()
    
    if "_" not in guess:
        break
    
    guessed.append(user)
            
if attempts <= 0:
    print(f"Game over! The word was: {word_get}")
else:
    print("Congratulations! You guessed the word.")