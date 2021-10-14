from random import randint
x = randint (1, 10)

y = input("Pick a number between 1 and 10, or press q to quit:")

a = int(y)

q = quit

while y != q:
    if a == y:
        print("good job!")
        break
    else:
        print("Guess again!")
        
        


