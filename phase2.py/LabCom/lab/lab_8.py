# 1
# key = input("Enter the key:\n")
# value = input("Enter the value:\n")
# print("Updated Dictionary:")
# print({key:value})

# 2
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# print("Concatenated Dictionary:")
# newdict = {}
# newdict.update(dic1)
# newdict.update(dic2)
# newdict.update(dic3)
# print(newdict)

# 3
# my_dict = {'apple': 3, 'banana': 1, 'cherry': 5}
# guess = input("Enter the key to check:\n")
# if guess in my_dict :
#     print("The key '{}' exists in the dictionary.".format(guess))
# else :
#     print("The key '{}' does not exist in the dictionary.".format(guess))

# 4
# my_dict = {'apple': 3, 'banana': 1, 'cherry': 5}
# print("Iterating over keys:")
# for k in my_dict.keys():
#     print(k)
# print()
# print("Iterating over values:")
# for v in my_dict.values():
#     print(v)
# print()
# print("Iterating over key-value pairs:")
# for k,v in my_dict.items():
#     print("Key:",k+",","Value:",v)

# 5
# number = int(input("Enter the value of n:\n"))
# newdict = {num: num**2 for num in range(1,number+1)}
# print("Generated Dictionary:")
# print(newdict)

# 6
# message = input("Enter a string:\n")
# print("Character Count in the String:")
# newlist = {char: message.count(char) for char in message}
# print(newlist)

# 7
# setA = (input("Enter elements for set 1 separated by spaces:\n"))
# setB = (input("Enter elements for set 2 separated by spaces:\n"))
# setA = setA.split()
# setB = setB.split()
# setA = set(setA)
# setB = set(setB)
# union = setA.union(setB)
# intersect = setA.intersection(setB)
# difference = setA-setB
# print("Union:",sorted(union))
# print("Intersection:",sorted(intersect))
# print("Difference (set1 - set2):",sorted(difference))

# 8.
# a = (input("Enter a list of numbers separated by spaces:\n"))
# b = a.split()
# c = set(b)
# lis = []
# for i in c :
#     if i in lis :
#         continue
#     lis.append(i)
# print("Unique numbers:",sorted(lis))

# 9.
# a = set(input("Enter the first word:\n"))
# b = set(input("Enter the second word:\n"))
# if a.issubset(b):
#     print("These words are anagrams!")
# else :
#     print("These words are not anagrams.")

# 10
# dic = {}
# even = {}
# time = int(input("Enter the number of key-value pairs:\n"))
# for i in range(1,time+1):
#     key = input("Enter key {}:\n".format(i))
#     value = int(input("Enter value for {}:\n".format(key)))
#     dic[key]= value
#     if int(value) %2 ==0 :
#         even[key] = value
# print()
# print("Original Dictionary:")
# print(dic)
# print()
# print("Dictionary of Even Numbers:")
# print(even)

# 11
# a = {int(e) for e in input("Enter a list of numbers separated by spaces:").split()}
# a = sorted(a)
# print()
# if len(a)< 3 :
#     print("Third largest number: There are less than three unique numbers in the list.")
# else :
#     print("Third largest number:",a[-3])
   
# 12
# sum = int(input("Enter the target sum:"))
# print(f"Unique combinations that add up to{sum}:")
# seto = set()
# for i in range(1,10):
#     for j in range(1,10):
#         for k in range(1,10):
#             if i+j+k == sum:
#                 x = i,j,k
#     seto.add(x)
# print(seto)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sum = int(input("Enter the target sum:"))
# print(f"Unique combinations that add up to{sum}:")
# def find_combinations(numbers, target):
#     s = set()
#     if target < 6 :
#         print(f"No unique combinations found that add up to {target}.")
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             for k in range(j + 1, len(numbers)):
#                 combination = (numbers[i], numbers[j], numbers[k])
#                 if sum(combination) == target:
#                     s.add(combination)

#     return s

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 15
# result = find_combinations(numbers, target)

# def find_combinations(numbers, target):
#     s = set()

#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             for k in range(j + 1, len(numbers)):
#                 combination = (numbers[i], numbers[j], numbers[k])
#                 if sum(combination) == target:
#                     s.add(combination)

#     return sorted(s)

# # Example usage:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = int(input("Enter the target sum:\n"))

# result = find_combinations(numbers, target)

# if result:
#     print(f"Unique combinations that add up to {target}:")
#     for combination in result:
#         print(combination)
# else:
#     print(f"No unique combinations found that add up to {target}.")


# result = []
# num = int(input("input :"))
# for i in range(1,10):
#     for j in range(i+1,10):
#         for k in range(j+1,10):
#             if i<j<k :
#                 if i+j+k == num :
#                     result.append((i,j,k))
# print(len(result))
# if len(result)!=0:
#     for item in result:
#         print(item)
# else :
#     print("maime")
