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
    bars_charged = bars_charged + 1
    print(f"Charging: {'█' * bars_charged}")

print("\nThe battery is fully charged!")





