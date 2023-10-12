import random
def display(answer, guessed_letter) :
    display = ""
    for letter in answer :
        if letter in guessed_letter :
            display += f"{letter} "
        else :
            display += "_ "
    return display
 
def answer_word() :
    words = ["cat", "dog", "chicken", "snake", "fish"]
    return random.choice(words)

def hangman() :
    guessed_letter = []
    attempts = 5
    digits = "0123456789"

    seed_value = int(input("Enter a seed: "))
    random.seed(seed_value)

    answer = answer_word()

    while attempts > 0 :
        print(display(answer, guessed_letter))
        guess = str(input("Enter a letter: "))
        
        if len(guess) !=1 :
            print("Please enter a single letter.")
            continue
        if guess in digits :
            print("Please enter a letter not digit")
            continue
        if guess in guessed_letter :
            print("You have guessed that letter")
            continue
        guessed_letter.append(guess)
        if guess in answer :
            print("correct")
        else :
            attempts -= 1
            print(f"Wrong! you have {attempts} attempts left")

        if "_ " not in display(answer, guessed_letter) :
            print("Congratulations!")
            break
        if attempts == 0 :
            print("you are out of attempt try again")
            break

hangman()
