import random

number = random.randint(1,100)

print("🎯 Guess the Number Game")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You won")
        break
    elif guess < number:
        print("Try bigger number")
    else:
        print("Try smaller number")