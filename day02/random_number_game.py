#using random number generators

import random #our random numbers are imported below

number = random.randint(1,20)
guess_number = 0 #here we are tracking the number of guesses by the user
while True: 
    guess = int(input("Guess what number I am thinking of, between 1 and 20: ")) #here we ask the user for input
    if guess < number:
        print("The number you guessed is too small, try again.")
    elif guess > number:
        print("The number you guessed is too big, try again.")
    else:
        print("Nice, you're correct!")
        guess_number += 1 # add 1 guess for the user being correct 
        break # here the game ends, if the user is correct

      guess_number += 1 # add a guess if the user is incorrect

print("The number of guesses it took you is: ", guess_number)

