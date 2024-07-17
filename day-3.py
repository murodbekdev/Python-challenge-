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