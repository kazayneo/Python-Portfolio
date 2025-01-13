#Number Guesser
#Catherine Li
#11/8/24

#Init
import random

#Functions

#This generates a random number for players to guess. The function will say if the number players input is correct or incorrect
def numberGuesser():
    print("Welcome to Guess The Number!")
    #x is an integer for players to guess
    x = random.randint(1,10)
    num = input("Please enter a number (1-10)") #this allows players to input a number to guess
    if num == x:
        print("Correct!")
    if num != x:
        print("Incorrect!" + " The correct number is " + str(x) + ".")

#Main

numberGuesser()
