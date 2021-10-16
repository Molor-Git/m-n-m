import random

print("______________________")
print("  M&M guessing game!")
print("______________________")

print("Guess the number of M&Ms and you get free lunch on the house!")
print()

mm_count = random.randint(1, 100)
attempts_limit = 5
attempts = 0

while attempts < attempts_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1
    if mm_count == guess:
        print(f"You got free lunch! It was {guess}.")
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")


print(f"Bye, you're done in  {attempts} attempts.")

