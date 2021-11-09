#!/usr/bin/env python3

from random import randint

import sys

class color:
    BOLD = '\033[1m'
    END = '\033[0m'

keep_track_of_rolls = []

def d20():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 20)
            print("You rolled", random_ng)
            if random_ng == 20:
                print(color.BOLD + "Heck yeah!" + color.END)
            if random_ng == 1:
                print(color.BOLD + "Aww, rats!" + color.END)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 20)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d6():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 6)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 6)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d100():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 100)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 100)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d8():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 8)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 8)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d10():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 10)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 10)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d12():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 12)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 12)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()

def d4():
    if number_of_rolls == 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            random_ng = randint(1, 4)
            print("You rolled", random_ng)

            repeat = input("Do you want to roll again? ")
        sys.exit()
    elif number_of_rolls > 1:
        repeat = "yes"
        while repeat == "yes" or repeat == "Yes" or repeat == "y":
            keep_track_of_rolls = []
            for i in range(number_of_rolls):
                random_ng = randint(1, 4)
                keep_track_of_rolls.append(random_ng)
            print("Individual rolls: ", keep_track_of_rolls)
            grand_total = sum(keep_track_of_rolls)
            print("Your total is: ", grand_total)

            repeat = input("Do you want to roll again? ")
        sys.exit()


valid_functions = ['d20', 'd6', 'd100', 'd10', 'd8', 'd12', 'd4']

try:
    #for terminal use, input dice type after dice_roller.py
    function = sys.argv[1]
    if function not in valid_functions:
        print("Not a valid function")
        sys.exit()

except IndexError:
    function = input("Which dice? ")

try:
    #input number of rolls in terminal, 2nd argument
    number_of_rolls = int(sys.argv[2])

except IndexError:
    number_of_rolls = int(input("How many rolls? "))




a = 'd20'
if function == a:
    d20()

b = 'd6'
if function == b:
    d6()

c = 'd100'
if function == c:
    d100()

d = 'd8'
if function == d:
    d8()

e = 'd10'
if function == e:
    d10()

f = 'd12'
if function == f:
    d12()

g = 'd4'
if function == g:
    d4()
else:
    print('Please enter a valid function, yo')
