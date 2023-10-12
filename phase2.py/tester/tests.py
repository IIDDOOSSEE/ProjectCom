# def print_date(year,month,*date):
#     print("Year:",year)
#     print("Month:",month)
#     for i in date :
#         if date == ():
#             return
#         else :
#             print("Date:",i)
    

# print_date(2023, 7)
# print()
# print_date(2023, 7, 24) 


# def sqrt_n_times(x,n):
#     ans = x**(1/2**n)
#     return ans
# print(sqrt_n_times(10**8,3))
    

# def cube_root(y):
#     a = sqrt_n_times(y,2)**(((((1+1/2**2)*(1+1/2**4)*(1+1/2**8)*(1+1/2**16)*(1+1/2**32)))))
#     return a
# print(round(cube_root(27),4))


# def main() :
#     q = float(input())
#     print(cube_root(q))
# main()
    
# ----------------------------------------------------

# def str2hms(hms_str):
#     t=hms_str.split(":")
#     return int(t[0]),int(t[1]),int(t[2])
# print(str2hms("10:05:07"))
    
# def hms2str(h,m,s):
#     return ("0"+str(h))[-2:] + ":" + \
#     ("0"+str(m))[-2:] + ":" +  ("0"+str(s))[-2:]
# print(hms2str(10,20,30))
# x = '10'
# print(x[-2:])


# def to_sec(h,m,s):
#     return(((h*3600)+(m*60)+s))

# def to_hms(s):
#     hr=s//3600
#     mi=(s-(hr*3600))//60
#     se=s-((hr*3600)-(mi*60))
#     return int(hr),int(mi),int(se)
# def diff (h1,m1,s1,h2,m2,s2):
    # import math
    # if h1 > 24 or h2 > 24 or m1 > 60 or m2 > 60 or s1 > 60 or s2 > 60:
    #     pass
#     hr = h2 - h1 
#     if m2 < m1 : 
#         h2 -=1
#         m2+=59
#         s2+=60
#     return int(h2-h1),int(m2-m1),int(s2-s1)
    
# def main():
#     hms_start = input()
#     hms_end = input()

#     h1, m1, s1 = map(int, hms_start.split(':'))
#     h2, m2, s2 = map(int, hms_end.split(':'))

#     t1 = h1 * 3600 + m1 * 60 + s1
#     t2 = h2 * 3600 + m2 * 60 + s2

#     ds = (t2 - t1 + 86400) % 86400
#     dh = ds // 3600
#     ds -= dh * 3600
#     dm = ds // 60
#     ds -= dm * 60
    
#     result = f"{dh:02d}:{dm:02d}:{ds:02d}"
    
#     print(result)
# main()
# exec(input())




# def split_text(text):
#     a = text.split(":")
#     return int(a[0]),int(a[1])
# x,y = split_text("10:5")
# print(x,y)

# number = (input("input num :"))
# while len(number)>1:
#     summation = 0
#     for  i in number :
#         summation+=int(i)
#     number = str(summation)
# print("summation for 1 digits:",summation)


message = ["dose","pao","saendee","tor","armmeen","arm","dodo","oreo","uno","meow","bew",]
import random

word = random.choice(message)
word_guess = ["_"]*len(word)
print("welcome to word guess game >>> G L H F <<<")
print(" ".join(word_guess))
change = 5
repeat = []
while change !=0 and "_" in word_guess :
    guess = input("guess the word : ")
    if guess in repeat :
        print("you had ever guess this alphabet try again !")
        break
    elif guess in word :
        for i in range(len(word)) :
            if guess == word[i]:
                word_guess[i] = guess
        print(" ".join(word_guess))
    else : 
        change -=1
        print(f"Stupid you miss your change is {change}")
    repeat.append(guess)
if "_" not in  word_guess:
    print("you won")
else : 
    print(f"you be loss the word was {word}")
