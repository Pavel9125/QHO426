import random

print("Please enter the min value: ")
minvalue = int(input())

print("Please enter the max value: ")
maxvalue = int(input())

ran_num = random.randrange(minvalue, maxvalue)

print(f"I'm thinking of a number between {minvalue} and {maxvalue}. Can you guess what it is? ")

num_guessed_correct = False

while not num_guessed_correct:
    print("Please enter number: ")
    user_entered = int(input())

    if user_entered == ran_num:
        print("Congratulations! You guessed my number!")
        num_guessed_correct = True

    elif user_entered < ran_num:
        print("Sorry, your guess is too low.")

    else:
        print("Sorry, your guess is too high.")

