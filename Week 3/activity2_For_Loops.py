print("How far are we from the target?")
distance = int(input())

print()

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("Target achieved!")