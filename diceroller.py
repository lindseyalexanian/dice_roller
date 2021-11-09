#!/usr/bin/env python3
from random import randint

import sys

class color:
    BOLD = '\033[1m'
    END = '\033[0m'

def d20():
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

def d6():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 6))

        repeat = input("Do you want to roll again? ")
    sys.exit()

def d100():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 100))

        repeat = input("Do you want to roll again? ")
    sys.exit()

def d8():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 8))

        repeat = input("Do you want to roll again? ")
    sys.exit()

def d10():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 10))

        repeat = input("Do you want to roll again? ")
    sys.exit()

def d12():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 12))

        repeat = input("Do you want to roll again? ")
    sys.exit()

def d4():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes" or repeat == "y":
        print("You rolled", randint(1, 4))

        repeat = input("Do you want to roll again? ")
    sys.exit()

try:
    #for terminal use, input dice type after dice_roller.py
    function = sys.argv[1]

except IndexError:
    function = input("Which dice? ")

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
