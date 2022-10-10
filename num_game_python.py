print("Welcome to Dave's Number Game!")

import random
number = random.randint(1,100) #random integer between 1 and 100
guess = 0 #stores the players guess
num_of_tries = 0 #keeps track of number to tries it takes to win

while guess != number: #loops while guess does not equal the number
    guess = int(input("Guess the number between 1 and 100:")) #gets user input as int
    num_of_tries += 1 #add 1 to number of tries each turn
    if guess == number:
        print("You guessed correctly! You Win!")
        print("It took you " + str(num_of_tries) + " tries to win.")
        break
    elif guess > number:
        print("You guessed too high")
    elif guess < number:
        print("You guessed too low")