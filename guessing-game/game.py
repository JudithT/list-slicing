"""A number-guessing game."""
import random

print("Hello there, Player!")
name = input("What is your name? ")
while True:
    try:
        start_num = int(input("Please pick a start number. "))
        end_num = int(input("Please pick an end number. "))
        break
    except ValueError:
        print("How silly of you! That's not an integer! Please enter an integer.")
        continue

num = random.randint(start_num, end_num)
num_guesses = 0
best_score = None
print("\n")
print(f"{name}, I'm thinking of a number between {start_num} and {end_num}.")
print("Try to guess my number.")

while True:
    num_guesses += 1
    try:
        guess = int(input("Your guess? "))
    except ValueError:
        print("How silly of you! That's not an integer! Please enter an integer.")
        continue
    if guess > end_num or guess < start_num:
        print("Whoops, that guess is out of range.")
    elif guess == num:
        if best_score == None:
            best_score = num_guesses
        elif best_score and (num_guesses < best_score):
            best_score = num_guesses
        print("Well done, {}! You found my number in {} tries!".format(name, num_guesses))
        print("Your best score is {}".format(best_score))
        cont = input("Would you like to continue? Y or N? ")
        while cont.lower() != 'y' and cont.lower() != 'n':
            print("Sorry, I don't know what you mean. Please enter Y or N.")
            cont = input("Would you like to continue? Y or N? ")
        if cont.lower() == 'y':
            num = random.randint(start_num, end_num)
            num_guesses = 0
            print("\n")
            print(f"{name}, I'm thinking of a number between {start_num} and {end_num}.")
            print("Try to guess my number.")
            continue
        elif cont.lower() == 'n':
            break
    elif guess > num:
        print("Too high, try again.")
    elif guess < num:
        print("Too low, try again.")
    if num_guesses == 10:
        print("Too many tries.")
        cont = input("Would you like to continue? Y or N? ")
        while cont.lower() != 'y' and cont.lower() != 'n':
            print("Sorry, I don't know what you mean. Please enter Y or N.")
            cont = input("Would you like to continue? Y or N? ")
        if cont.lower() == 'y':
            num = random.randint(start_num, end_num)
            num_guesses = 0
            print("\n")
            print(f"{name}, I'm thinking of a number between {start_num} and {end_num}.")
            print("Try to guess my number.")
            continue