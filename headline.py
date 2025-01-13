#Clickbait Headline Generation
#Catherine Li

#Init

#Functions
def giftHeadline():
    num = input("Please enter a number (1-99)")
    noun = input("Please give me a name")
    state = input("Please give me a state")
    print(str(num) + " Gift Ideas To Give Your " + noun + " From " + state)

def doctorHeadline():
    num = input("Please enter a number (2-50)")
    noun = input("Please enter a name")
    state = input("Please enter a state")
    print("Doctors Hate Him! " + str(num) + " Ways " + noun + " Does to Jeopordize Their Health in " + state)

def wantedHeadline():
    num = input("Please enter a number(10-20)")
    state = input("Please enter a state")
    print("Danger Alert! Top " + str(num) + " Wanted Criminals In " + state)

#Main
giftHeadline()
doctorHeadline()
wantedHeadline()
