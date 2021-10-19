
from random import randint
x = randint (1, 30)

while True:
        try:
            guessed = int(input("Pick a number between 1 and 30:"))
        except ValueError:
            print("No. Only integers please. Pick a number between 1 and 30:")                     
        if x == guessed:
            print("Well done, good job!")
            break
        elif x > guessed:
            print("guess again, try higer")
        else:
            print("guess again, try lower")
        
        