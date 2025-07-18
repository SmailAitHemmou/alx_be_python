print("I'm thinking of a number between 1 and 10. Can you guess it?")
# This code generates a random number between 1 and 10
import random
random_number = random.randint(1, 10)
guess_count = 0
# This code allows the user to guess the number
while True:
    number = int(input("enter a number betwen 1 and 10: "))
    guess_count += 1

    print(f"Your choice is", str(number) + " and the random number is ", str(random_number))
    if number< 1 or number > 10:
        print("Sorry, that's not correct. Try again!")
        continue
    if random_number == number:
        print(f"Congratulations, you guessed it! It took you {guess_count} tries.")
        break
    elif random_number < number:
        print("Oops, your guess is a bit high. Try again!")
    else :
        print("Oops, your guess is a bit low. Try again!")
print("Play again? (Yes/No)")
user_answer = input("Enter your answer: ")
if user_answer.lower() == "yes":
    print("Great! Let's play again!\n ... (new game starts)")
else:
    print("Thanks for playing! Goodbye!")