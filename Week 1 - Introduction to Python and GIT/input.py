#Input
surname = input("Please enter your surname:") # Ask user for surname
firstname = input("Please enter your firstname:") # Ask user for firstname
numLucky = float(input("Please enter your lucky number: ")) # Ask user for Lucky number
#Let's add 10 to the lucky number
#numNew = numLucky+10
#print(numNew)
#print("your full name is :", surname, firstname)
#print("Your lucky number is :", numLucky)
#print("Your unique password is:", surname,numLucky)
#print(f"Your unique password is: {surname}{numLucky}")
if numLucky >= 37:
    print("Your number is greater than 37.")
elif numLucky == 500:
    print("Your number is 37.")
else:
    print("Your number is less than 37.")








