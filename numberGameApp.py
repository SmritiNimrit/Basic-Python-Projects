import random

#generate a random number between 1 to 10
secret_number = random.randint(1,10)

#putting the game in a function
def run_game():
    guesses = []
    guess = 0

    #limit the number of guesses to 5
    while len(guesses) < 5:
        
        #catch if someone submits a non-integer value
        try:
            #get a number from player
            guess = int(input("Guess a number between 1 to 10: "))
        except ValueError:
                print("{} isn't a number!".format(guess))
        else:
                #compare guess with the secret number
                if guess == secret_number:
                     #print hit/miss
                    print("You got it!. My number was {}".format(secret_number))
                    break

                #print "too high" or "too low"
                elif guess < secret_number:
                    print("My number is higher than {}".format(guess))
                elif guess > secret_number:
                    print("My number is lower than {}".format(guess))
                
                else:
                    #print hit/miss
                    print("That's not it!")

        guesses.append(guess)
    else:
        print("You didn;t get it!. My number was {}".format(secret_number))

    play_again()

   

def welcom():
    print("Welcom to the letter guess game!!!")
    run_game()

def play_again():
     #let people play again
    play_more = input("Do you want to play again? [y/n]")

    if play_more.lower()!= 'n':
        run_game()
    else:
        print("Bye!!!")

welcom()



 
    
            