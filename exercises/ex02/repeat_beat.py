"""Repeating a beat in a loop."""

__author__ = "730390434"


user_beat: str = input("What beat do you want to repeat? ")

number_of_repeat: int = int(input("how many times do you want to repeat it? "))

number_of_repeat: int = (number_of_repeat - 1)

print((user_beat + " ") * (number_of_repeat) + user_beat)

if number_of_repeat <= 0:
    print("No beat...")