#Catherine Li
#1/9/25
#Multiplication Game

#Init
import random
points = 0 #int

#Functions
#This is for the easy level questions of the game
def easyLevel():
    global points
    num1 = random.randint(0,5) #int
    num2 = random.randint(0,5) #int
    print("What is " + str(num1) + " x " + str(num2) + "?")
    ans = input(str("Your answer:"))
    if ans == str(num1*num2):
        points = points + 1
        print("Congrats, you got it right! Your score is now " + str(points) + "!")
    else:
        print("Sorry! That answer was wrong.")

#This is for the medium level questions of the game
def midLevel():
    global points
    num1 = random.randint(5,10)
    num2 = random.randint(5,10)
    print("What is " + str(num1) + " x " + str(num2) + "?")
    ans = input(str("Your answer:"))
    if ans == str(num1*num2):
        points = points + 2
        print("Congrats, you got it right! Your score is now " + str(points) + "!")
    else:
        print("Sorry! That answer was wrong.")

#This is for the hard level questions of the game
def hardLevel():
    global points
    num1 = random.randint(10,20)
    num2 = random.randint(10,20)
    print("What is " + str(num1) + " x " + str(num2) + "?")
    ans = input(str("Your answer:")) #int
    if ans == str(num1*num2):
        points = points + 3
        print("Congrats, you got it right! Your score is now " + str(points) + "!")
    else:
        print("Sorry! That answer was wrong.")

#This function codes the actual game
def multiplicationGame(questions):
    while true:
        global points
        print("Hello! Welcome to the multiplication game!")
        level = input("Choose a level: easy, medium, or hard!") #str for how difficult the questions will be
        level = level.lower()
        if level == "easy":
            for i in range(questions):
                easyLevel()
        if level == "medium":
            for i in range(questions):
                midLevel()
        if level == "hard":
            for i in range(questions):
                hardLevel()
        loop = input("Do you want another round? (yes,no)") #str for whether or not the player wants to continue playing
        loop = loop.lower()
        if loop == "yes":
            print("Alright! Welcome to a new game!")
        if loop == "no":
            print("Alright! Goodbye, player!")
            break


#Main
multiplicationGame(questions)
