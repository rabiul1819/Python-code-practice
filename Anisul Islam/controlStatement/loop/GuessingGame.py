from random import randint

guessNumber = int(input("Guess a number between 1 and 5: "))

randomNumber = randint(1,5)
if guessNumber == randomNumber:
    print(f"You have Won!")
else:
    print(f"You have Lose!.")