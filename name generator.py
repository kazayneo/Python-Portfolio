#18 Name Generator

#This script asks the player (mostly) food-related questions in order to generate the name of a Sanrio character that best fits their answers.
print("Welcome to the Sanrio Name Generator! Answer these questions to find out your ideal Sanrio character!")
ans = input("Summer or Winter?") #string. this is the first question that starts the quiz
if ans == "Summer":
    ans = input("Strawberries or Blueberries?")
    if ans == "Strawberries":
        ans = input("Candy or Cake?")
        if ans == "Cake":
            print("Your Sanrio character is My Melody!") #answer 1
        else:
            print("Your Sanrio character is Hello Kitty!"); #answer 2
    else:
        ans = input("Tea or Ice Cream?")
        if ans == "Tea":
            print("Your Sanrio character is Tuxedo Sam!") #answer 3
        else:
            print("Your Sanrio character is Usahana!"); #answer 4
if ans == "Winter":
    ans = input("Rabbit or Dog?")
    if ans == "Rabbit":
        ans = input("Cherries or Cinnamon Rolls?")
        if ans == "Cherries":
            print("Your Sanrio character is Kuromi!") #answer 5
        else:
            print("Your Sanrio character is Cinnamoroll!"); #answer 6
    else:
        ans = input("Sports or Sleep?")
        if ans == "Sports":
            print("Your sanrio character is Pochacco!") #answer 7
        else:
            print("Your sanrio character is Pompompurin!"); #answer 8
