import random
import os
import sys

#make a list of words
words = [
    'apple',
    'banana',
    'coconut',
    'orange',
    'blueberry',
    'strawberry',
    'pineapple',
    'mango',
    'dragonfruit'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    # os.system('cls' if os.name == 'nt' else: 'clear') 

def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print("Strikes: {}/7".format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end='')
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_',end='')

def get_guess(bad_guesses,good_guesses):
    while True:
        print('')
        guess = input("Guess a letter: ").lower()

        if len(guess)!=1:
            print("You can only guess a single letter")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters")
        else:
        
            return guess

def play(done):
    clear()

    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
     
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found=False

            if found:
                print("You won!")
                print("The secret word was {}".format(secret_word))
                done=True

        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("\n You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? [y/n]").lower()

            if play_again!='n':
                return play(done=False)
                  
            else:
                print("Hope to see you soon...Bye!")
                sys.exit()

def welcome():
    start = input("Press enter/return to start or 'q' to quit: ")
    if start == 'q':
        print("Bye!!!")
        sys.exit()
    else:
        return True

clear()
print("Welcome to letter game!")
done = False
while True:
   
    welcome()
    play(done)



