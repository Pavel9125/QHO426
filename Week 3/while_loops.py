#Activity 1: Simple loop
#Tast

print("How many apples should I remove?")
user_remove = int(input())
removed = 0
print()
while removed < user_remove:
    print(f"{removed+1} Removed Apple")
    removed = removed +1

# Activity 2: Count
#Task

print("How many obstacles must I avoid?")
obstacle_avoid = int(input())

avoided_obstacles = 0
while avoided_obstacles < obstacle_avoid:
    print("Avoiding...", end="")
    avoided_obstacles = avoided_obstacles + 1
    print(f"Done! {avoided_obstacles} obstacles avoided.")

print("\nAll obstacles have been avoided!")

#Activity 3: ASCII
#Task
print("How many bars should be charged?")
charged_bars = int(input())
bars_charged = 0
while bars_charged < charged_bars:
    #print("Charged...", end="")
    bars_charged = bars_charged + 1
    print(f"Charging: {'█' * bars_charged}")

print("\nThe battery is fully charged!")

#Activity 4: Repeating Word
#Task
print("Please enter a phrase")
phrase = input()
hello = 0
while hello < len(phrase):
    print("Hi ", end="")
    hello = hello + 1

#Activity 5: Sum 100
#Task
print("Calculate the sum of the first 100 numbers...")
i = 1
total = 0

while i <= 100:
    total += i
    i += 1

print("...Done! The answer is", total)

#Activity 6: Sum User Numbers
#Task
number_count = int(input("How many numbers should I sum up?\n"))
total_sum = 0
current_number = 1
while current_number <= number_count:
    num = int(input(f"Please enter number {current_number} of {number_count}: "))
    total_sum += num
    current_number += 1
print("\nThe answer is", total_sum)








