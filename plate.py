answer = "Y"

while answer.upper() == "Y":

    reply = input(
        """Can you tell me how much food is there on your plate? Is it...
 Full, half or 0?
            Please enter..."""
    )

    if reply.upper() == "FULL":
        print("I will give you a cooti now!! 👋👋")
    elif reply.upper() == "HALF":
        print("Make it 0, otherwise, I will give you a cooti! 🫥")
    elif reply == "0":
        print("Good boy! Good! 😊")
    else:
        print("What the hell have you typed you Bhappu Bhabundri 😶???")

    answer = input(
        "Do you want to tell me how much food is there on your plate again? (Y/N)"
    )

print("Bye,bye, thank you for telling me how much food is there on your plate!")

print("Also, remember to eat more healthy food! 🍛👍🏻")
