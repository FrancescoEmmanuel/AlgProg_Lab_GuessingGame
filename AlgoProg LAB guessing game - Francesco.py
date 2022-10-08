
import random

randomint = random.randint(1,100) 
guess=0
tries= 0

while guess != randomint:
    tries+=1
    guess = int(input("Try and guess a random interger from 1-100: "))

    if guess == randomint:
        print(f"Correct! The interger is {randomint}, it only took you like {tries} guesses.")
    elif (guess > randomint):
        print("Too high! Try again bruh ")
    else:
        print("Too low! Try again bruh ")
    
    if tries>=10:
        print("You're so bad at this, please get help!")


