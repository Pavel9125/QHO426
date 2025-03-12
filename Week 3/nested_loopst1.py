print("How many Rows would you like?: ")
rows = int(input())
print("How many Columns would you like?: ")
columns = int(input())
print("Here I go: \n")
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":)", end=" ")
    print()
print("\nDone!")


