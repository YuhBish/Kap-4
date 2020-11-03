import random

guess = 0
correct = random.randint(1, 1000000)
while guess != correct:
    guess = int(input("Gissa rätt tal: "))

    if guess < correct:
        print("för lite")
    
    elif guess > correct:
        print("för mycke")
print ("rätt")
