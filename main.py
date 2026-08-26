import random

number = random.randint(1, 20)
attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess my number(1,20): "))
    # if the guess too high
    if guess > number:
        print("Too High take a lower")
        # if guess too low
    elif guess < number:
        print("Too Low take a higher")
        # when person guess it
    if guess == number:
        print(f"You guessed, my number is {number}")
        # attempts
        print(f"Your attempts are {attempts}")
        break
