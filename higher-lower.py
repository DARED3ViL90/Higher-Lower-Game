
from random import randint
x = randint (1, 10)

while True:
    try:
        guessed = input("Pick a number between 1 and 10:")

    except ValueError:
        print("Please use a number between 1 and 10. Thank you.")
    guessed = int(guessed)

    if x == guessed:
        print("Well done, good job!")
        break
    elif x > guessed:
        print("guess again, try higer")
    else:
        print("guess again, try lower")

