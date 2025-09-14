from random import randint

rock = 0
paper = 1
scissors = 2

winner = ""

computer_guess = randint(0, 2)

print("Welcome to Karman's Rock, Paper, Scissors game!")
print("Rock, paper, scissor, shoot!")

user_guess = (
    int(
        input(
            """Please pick one:
                       1. Rock
                       2. Paper
                       3. Scissors
                       """
        )
    )
    - 1
)

print(f"Computer guess: {computer_guess}")
print(f"User guess: {user_guess}")

if user_guess == rock:
    if computer_guess == rock:
        winner = "draw"
    elif computer_guess == paper:
        winner = "computer"
    else:
        winner = "user"

elif user_guess == paper:
    if computer_guess == rock:
        winner = "computer"
    elif computer_guess == paper:
        winner = "draw"
    else:
        winner = "computer"

elif user_guess == scissors:
    if computer_guess == rock:
        winner = "computer"
    elif computer_guess == paper:
        winner = "user"
    else:
        winner = "draw"

print(f"The winner is {winner} 🕶️")
