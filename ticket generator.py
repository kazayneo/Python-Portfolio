#Catherine Li
#12/11/24

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

#Code by Catherine Li
#Calulates the ticket price, and draws out the ticket with the buyer's name, day of week, and price
def ticket():
    name = input("Please enter your name")
    dayofweek = input("What day of the week are you visiting?")
    age = int(input("Please enter your age"))
    if age < 4:
        price = 0 #Price is the integer that the buyer needs to pay for entry
    if age > 3 and age < 18: 
        if dayofweek == "Sunday" or dayofweek == "Saturday":
            price = 100
        else:
            price = 50
    if age > 17:
        price = 100
    coupon = input("Do you have a coupon? Enter it here") #coupon = string, for the code that buyers can put in to discount the price
    if coupon == "FREEFRIDAY" and dayofweek == "Friday" and age < 18:
        price = 0
    if coupon == "SUNDAY10" and dayofweek == "Sunday" and age < 18:
        price = price - 10
    y_location = 0 #y location is set to 0 to make the placement of the ticket consistent
    draw_ticket(name, price, dayofweek, y_location)

#Main

#2. Collect info
#Name, age, day of the week, coupon

# Algorithm for determining price


ticket()
