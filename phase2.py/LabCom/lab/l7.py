# 1
# a = [e for e in input("Enter a list of characters separated by spaces:\n").split()]
# x = ""
# for i in range(len(a)) :
#     x = x+a[i]
# print("Converted string:",x) 

# # 2
# lis = []
# a = [int(e) for e in input().split()]
# for i in range(len(a)) :
#     lis.append(i*a[i])
# print("Modified tuple:",tuple(lis))

# 3
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers[::-1]:
#     print(i)

# 4
# lis1 = []
# lis2 = []
# a = [e for e in input("Enter elements for list 1 (space-separated):\n").split()]
# b = [e for e in input("Enter elements for list 2 (space-separated):\n").split()]
# print("List1:",a)    
# print("List2:",b+a)

# 5
# a = input("Enter the words separated by spaces:\n").split()
# for i in a :
#     print("Lenght of",i+":",len(i))

# 6
# import random
# population = ['red', 'blue', 'green', 'yellow', 'orange']
# for seed_value in range(1,11):
#     random.seed(seed_value)
#     lis = []
#     lis.append(random.choice(population))
#     print("Seed:",str(seed_value)+",","Random Sample:",lis)

# 7
# lis = []
# a = input("Enter words seperated by spaces:\n").split()
# for i in a :
#     lis.append(i[0])
# print("First characters:",lis)

# 8
# a = input("Enter a list of numbers seperated by spaces:\n").split()
# def remove_even(b):
#     lis = []
#     for i in b :
#         if int(i) % 2 != 0:
#             lis.append(int(i))
#     return lis 
# print(remove_even(a))

# 9
# a = input("Enter the first list of elements separated by spaces:\n").split()
# b = input("Enter the second list of elements separated by spaces:\n").split()
# def check(lis1,lis2):
#     for i in lis1:
#         if i in lis2 :
#             return True
# print(b)
# if check(a,b):
#     print("The lists have at least one common member.")
# else :
#     print("The lists do not have any common members.")  

# 10
# a = [e for e in input("Enter elements for the first list separated by spaces:\n").split()]
# b = [e for e in input("Enter elements for the second list separated by spaces:\n").split()]
# lis = []
# for i in range(len(a)):
#     x = a[i],b[i]
#     lis.append(x)
# print("Combined list of tuples:",lis)

# 11
# import random
# a = input("Enter a seed for the random number generator: Welcome to Hangman!\n")
# random.seed(a)
# data  = ["python", "hangman", "programming", "computer", "challenge", "learning"]
# attempts = 6
# word = random.choice(data)
# word_guess = ["_"]*len(word)
# print("".join(word_guess))
# ever_guess = []
# while attempts != 0 and "_" in word_guess:
#     guess = input()
#     if guess in ever_guess:
#         print("You already guessed that letter.")
#         continue
#     elif guess in word :
#         for i in range(len(word)):
#             if word[i] == guess:
#                 word_guess[i] = guess
#         print("".join(word_guess))
#     else :
#         attempts-=1
#         print("Guess a letter: Wrong guess!",f"You have {attempts} left.")
#         continue
#     ever_guess.append(guess)
# if "_" not in word_guess :
#     print("Congratulations! You guessed the word.")        
# else : 
#     print("Game over! The word was:",word)
        