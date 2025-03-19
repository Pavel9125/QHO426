print("Program Started!")
num1=int(input("Please enter an ASCII code: "))
while num1 not in range(32,126):
    print("Enter a valid number")
    num1=int(input("Please enter a valid ASCII code: "))

print(chr(num1))

