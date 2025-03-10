#Activity 3:Data Types
#Task
print("Whats is your name? ")
name = input()
print("How old are you? ")
age = int(input())
print("How tall are you?(in meters) ")
height = float(input())
print("How much do you weigh?(in kilograms) ")
weight = float(input())
BMI1 = weight / (height **2)# this will show the whole number
BMI= weight / (height ** 2) # this and the next 2 lines will make the number round to 2 decimal numbers
BMI_rounded2 = round(BMI, 2)
BMI= round( (weight / (height **2)), 2)
print(f"{name} you are is {age} years old and your BMI is {BMI_rounded2} ")
print(f"{name} you are is {age} years old and your BMI is {BMI} ")
print(f"{name} you are is {age} years old and your BMI is {BMI1} ")