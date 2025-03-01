#Input
surname = input("Please enter your surname:")
firstname = input("Please enter your firstname:")
numLucky = int(input("Please enter your lucky number: "))
#Let's add 10 to the lucky number
numNew = numLucky+10
print(numNew)
print("your full name is :", surname, firstname)
print("Your lucky number is :", numLucky)
print("Your unique password is:", surname,numLucky)
print(f"Your unique password is: {surname}{numLucky}")


