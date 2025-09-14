from random import randint

answer = "Y"
num_tries = 3

while answer.upper() == "Y":
    random_num = randint(1, 10)

    print(
        "I have thought of a number between 1 to 10 & you have to guess it in 3 tries."
    )

    correct = False

    for i in range(num_tries):
        tries_left = num_tries - i

        if tries_left == 1:
            guess = int(
                input(f"Guess the number (only {tries_left} try remaining 😱😱): ")
            )
        else:
            guess = int(input(f"Guess the number ({tries_left} tries remaining): "))

        if guess < 1 or guess > 10:
            print("Your guess should be between 1 and 10 😡😡")
        elif guess == random_num:
            print("You guessed it SIR 🥳")
            correct = True
            break
        elif guess > random_num:
            print("Wrong 🙁 Lesser number please.")
        elif guess < random_num:
            print("Wrong 🙁 Bigger number please.")

    if correct == False:
        print("Sorry, you could not guess the number 😞")
        print(f"The number was {random_num} SIR 😎")

    answer = input("Do you want to play again? (Y/N) ")

print("Thank you for playing Karman's guessing game! 😎")