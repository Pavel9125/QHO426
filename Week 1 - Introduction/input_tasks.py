# Activity 1: Reading user input

#Task
# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

#Activity 2: ASCII Robot
#Task

print("Please enter Character for eye")
eye = input()
print(f'''
##########
# {eye}    {eye} #
#  ----  #
##########''')

#Activity 3:Data Types
#Task
print("Whats is your name?")
name = input()
print("How old are you?")
age = int(input())
print("How tall are you?(in meters)")
height = float(input())
print("How much do you weigh?(in kilograms)")
weight = float(input())
BMI1 = weight / (height **2)# this will show the whole number
BMI= weight / (height ** 2) # this and the next 2 lines will make the number round to 2 decimal numbers
BMI_rounded2 = round(BMI, 2)
BMI= round( (weight / (height **2)), 2)
print(f"{name} you are is {age} years old and your BMI is {BMI_rounded2} ")
print(f"{name} you are is {age} years old and your BMI is {BMI} ")
print(f"{name} you are is {age} years old and your BMI is {BMI1} ")


# Activity 4: String Operator
# Task

print("Please enter the number of lives")
lives = int(input())
print("Please enter energy level")
energy = int(input())
print("Please enter shield level")
shield = int(input())

#Bot Data
print(f"Lives: {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")
