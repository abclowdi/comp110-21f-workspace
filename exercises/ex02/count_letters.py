"""Counting letters in a string."""

__author__ = "730390434"


from typing import Counter

letter = input("What letter do you want to search for?: ")
word = input("Enter a word: ")
i: int = 0
count: int = 0
# counter(letter)
while i < len(word):
    if word[i] != letter:
        i = i + 1
    else:
        if word[i] == letter:
            count = count + 1
            i = i + 1
            print(count)