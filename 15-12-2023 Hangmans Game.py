import random
# from tkinter import *


# w = Tk()
# w.title("Hangman (Let's Play!)")
# w.geometry("600x400")
           
def display_name(name, guessed_letters):
    display = ''
    for letter in name:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    names = ['prabhas', 'raviteja', 'alluarjun', 'hrithik', 'rana']  
    word_to_guess = random.choice(names)
    guessed = []
    attempts = 3 

    print("Let's play a Hangman's Game!")
    print(display_name(word_to_guess, guessed))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You've already guessed that letter!")
            continue

        guessed.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)
            if attempts == 0:
                print("You lost! The Hero name is :", word_to_guess)
                break
        else:
            print("Good guess!")
        
        display = display_name(word_to_guess, guessed)
        print(display)

        if '_' not in display:
            print("Congratulations! You've guessed the hero name:", word_to_guess)
            break

hangman()
