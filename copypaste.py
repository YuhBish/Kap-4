import random

guess = 0
guesses = 0
number = random.randint (0, 1000000)

while guess != number:
    guesses += 1
    guess = random.randint (0, 1000000)
print (f"Amount of tries: {guesses} ")
print (f"The number was: {number}")

if guesses > 3000000:
    print ("wow many gues")

if guesses < 10000:
    print ("wow few gues")

if number > 999000:
    print ("wow big nomber")

if number < 10000:
    print ("wow smol nomber")