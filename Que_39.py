"""
Write a program able to play the "Guess the number"-game, where the number to
be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com)
This is how it should work when run in a terminal:
>>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
"""

import random


def guessTheNumber():
    trials_count = 1
    secretNumber = random.randint(1, 20)

    while True:
        userName = input("Hello! What is your name?\n")
        print("Well, %s, I am thinking of a number between 1 and 20."%(userName))
        userNumber = input("Take a guess.\n")
        if userNumber == "exit":
            break
        else:
            
            userNumber = int(userNumber)
            while userNumber != secretNumber:

                if userNumber > secretNumber:
                    print("Too high!")

                elif userNumber < secretNumber:
                    print("Too low!")

                trials_count += 1
                userNumber = int(input("Take a guess.\n"))

            if trials_count == 1:
                print("Good job, %s! You guessed my number at the first try!"%(userName))
            else:
                print("Good job, %s! You guessed my number in %s guesses!"%(userName, trials_count))
                break

            

if __name__ == '__main__':
    guessTheNumber()
