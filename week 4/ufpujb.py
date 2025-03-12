#number_count = int(input("How many numbers should I sum up?\n"))
#total_sum = 0
#current_number = 1
#while current_number <= number_count:
   # num = float(input(f"Please enter number {current_number} of {number_count}:\n"))
  #  total_sum += num
 #   current_number += 1
#print("\nThe answer is", total_sum)


weight = input("Weight: ")
input ("(K)g or (L)bs: ")
if input() == "k" or "K":
    print("\n Your weight in kg is ", weight)
elif weight.lower() == "l" or "L":
    print("\n Your weight in lbs is ", weight)
else:
    print("\n Wrong input")
