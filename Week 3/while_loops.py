#Activity 1
#Tast

print("How many apples should I remove?")
user_remove = int(input())
removed = 0
print()
while removed < user_remove:
    print(f"{removed+1} Removed Apple")
    removed = removed +1

# Activity 2
#Task

print("How many obstacles must I avoid?")
obstacle_avoid = int(input())

avoided_obstacles = 0
while avoided_obstacles < obstacle_avoid:
    print("Avoiding...", end="")
    avoided_obstacles = avoided_obstacles + 1
    print(f"Done! {avoided_obstacles} obstacles avoided.")

print("\nAll obstacles have been avoided!")


