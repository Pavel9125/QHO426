print("Please enter a sequence")
user_sequence = input()
print("Please enter the character for the marker")
user_marker = input()

#marker1_p=0
#marker2_p=0
counting = False
count = 0


#for marker_p in range (0, len(user_sequence), 1):
for character in user_sequence:
    if (counting == False) and (character == user_marker):
        print("First Marker")
        counting = True
    elif (counting == True) and (character == user_marker):
        print("Second Marker")
        counting = False
    elif counting:
        count += 1
print(f"The total characters between the markers are {count}")

