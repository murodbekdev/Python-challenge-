# Day 3

# We are gonna learn about Conditional Statements, Logical Operators, Code Blocks and Scope


"""
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rolleercaoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif (age <18):
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be OK. Have a free ride on us")
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")  # Adding a photo condition, if yes $3 adds to the bill
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride!")

"""







"""
number = int(input("Enter a number here "))

if number % 2 == 0:
    print("It is even")
else:
    print("It is odd")

"""



# BMI Calculator


# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# age = int(input("Enter your current age: "))


""" 
bmi_calculator =  round(weight / height ** 2)

if bmi_calculator < 18.5:
    print(f"Your bmi is {bmi_calculator}, you are underweight")
elif bmi_calculator < 25:
    print(f"Your bmi is {bmi_calculator}, you have a normal weight")
elif bmi_calculator < 30:
    print(f"Your bmi is {bmi_calculator}, you are overweight")
elif bmi_calculator < 35:
    print(f"Your bmi is {bmi_calculator}, you are obese")
else:
    print(f"Your bmi is {bmi_calculator}, are clinically obese")

"""


"""

# Leap Year

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap yaer")
else:
    print("Not leap year")
"""

"""

# Pizza order challenge
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?, S, M, L: ")
add_peperroni = input("Do you want pepperoni?, Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

# Here i can declare the size with if condition
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25
# Here is i can use a nested if statement
if add_peperroni == "Y":
    if size == "S":
        bill += 2
    else:
        bill+=3

        # Here is if the user chooses extra cheese for Pizza, it will add another dollar
if extra_cheese == "Y":
    bill+=1

print(f"Your total bill is ${bill}")
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names_string = name1 + name2
lower_case_string = combined_names_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e
if love <= 10:
    true = true + 1
    love = 0
love_score = int(str(true) + str(love))  # why is it str()  cause string adds together not mathenatics, if it will be int() it i'd be 8

# print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif (love_score >=40) and (love_score <= 50):
    print(f"Your score is {love_score}%, you are alright together.")

else:
    print(f"Your score is {love_score}%")



# Treasure Game

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')



# So here we can start the if conditions

right_or_left = input('You\'re at a cross road. Where do you want to go? Type "left" or "right". ')
if right_or_left == "left":
    wait_or_swim = input("You come to a lake. There is on island in the middle ot the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if wait_or_swim == "wait":
        red_or_blue_or_yellow = input("You arrive at the island unharmed. There is a house with 3 doors. One red, on yellow and one blue. Which color do you choose?")
        if red_or_blue_or_yellow == "yellow":
            print("You win the Treasure Island Game, Gongratulations!!!")
        else:
            print("You enter a room of boasts. Game over.")
    else:
        print("You enter a room of boasts. Game over.")

else:
    print("You enter a room of boasts. Game over.")
    print("This repl has exited, run again?")