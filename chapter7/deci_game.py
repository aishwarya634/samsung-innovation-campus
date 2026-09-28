import math
print(math.sin(1))
import chart
x=[1,2,4,3,3,1,7,9,9]
chart.histogram(x)

import module

print(module.add(10, 20))
print(module.subtract(20, 5))
print(module.name)

import random 
z=[2,3,6,5]
print(random.randrange(10,20,1))
print(random.randint(10,23))
print(random.random())
print(random.uniform(10,20))

import random
import time


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)

    print("Computer total:", computer_total)
    print("User total:", user_total)

    if user_total > computer_total:
        print("User wins")
    elif user_total < computer_total:
        print("Computer wins")
    else:
        print("It is a tie!")


def roll_again(choices, dice_list):
    print("Rolling again ...")
    time.sleep(3)

    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1, 6)

    time.sleep(3)


def computer_strategy1(n):
    print("Computer is thinking ...")
    time.sleep(3)

    choices = ''

    for i in range(n):
        choices = choices + 'r'

    return choices


def computer_strategy2(n):
    print("Computer is thinking ...")
    time.sleep(1)

    choices = ''

    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + 'r'
        else:
            choices = choices + '-'

    return choices


# S1 start game
number_dice = input("Enter number of dice: ")
number_dice = int(number_dice)

ready = input("Ready to start? Hit any key to continue")

# S2 roll dice
user_rolls = roll_dice(number_dice)
print("User first roll:", user_rolls)

# S4 user choice
user_choices = input("Enter - to hold or r to roll again: ")

#if user enters other symbols
while len(user_choices) != number_dice or any(c not in "-r" for c in user_choices):
    print("Invalid input!")
    print("Enter only '-' or 'r'.")
    user_choices = input("Enter - to hold or r to roll again: ")

# Check length of user input 
while len(user_choices) != number_dice:
    print("You must enter", number_dice, "choices")
    user_choices = input("Enter - to hold or r to roll again: ")

# S5 reroll of the user
roll_again(user_choices, user_rolls)
print("Player new Roll:", user_rolls)

# Computer's roll
print("Computers turn")
computer_rolls = roll_dice(number_dice)
print("Computer first roll:", computer_rolls)

# S6 computer stratergy
computer_choices = computer_strategy2(number_dice)
print("Computer Choice:", computer_choices)

roll_again(computer_choices, computer_rolls)
print("Computer new Roll:", computer_rolls)

# winner
find_winner(computer_rolls, user_rolls)


