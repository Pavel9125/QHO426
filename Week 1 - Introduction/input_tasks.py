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
#  ---- a #
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
BMI= weight / (height ** 2)
BMI_rounded2 = round(BMI, 2)
print(f"{name} you are is {age} years old and your BMI is {BMI_rounded2} ")



