"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730390434"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


guess = randint(0, 10)

print("Your fortune cookie says... ")

if guess == 5:
    print("You will run into an old friend soon! ")
else:
    if guess > 5:
        print("You will run into a great sum of money soon! ")
    else: 
        print("You will acomplish great things! ")
        if guess == 2:
            print("Today is your lucky day! ")

print("Now, go spread positive vibes! ")