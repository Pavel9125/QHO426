#Input
surname = input("Please enter your surname:")
firstname = input("Please enter your firstname:")
numLucky = input("Please enter your lucky number: ")
print("your full name is :", surname, firstname)
print("Your lucky number is :", numLucky)
print("Your unique password is:", surname+numLucky)
print(f"Your unique password is: {surname}{numLucky}")


