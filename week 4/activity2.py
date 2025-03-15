print("Program Started!")
num1=int(input("Please enter an ASCII code: "))
while num1 not in range(32,126):
    print("Enter a valid number")
    print(chr(num1))

