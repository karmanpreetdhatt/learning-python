answer = "Y"

while answer.upper() == "Y":
    print("Computer: Stay very still! Don't move a muscle!")

    answer = input("Computer: Is the monster friendly? (Y/N): ")

    if answer.upper() == "Y":
        print ("Computer: Whew! You're safe!")

    elif answer.upper() == "N":
        print("Monster: Roar! Ha-ha!")
        print ("Computer: Uh-oh! Run away! Go, go!")
        print("Human: Aack! I can't survive!")
        print("Human: I am very scared!")
        print("Monster: Roar! Ha-ha!")

    else:
        print("Computer: I didn't understand that answer. Assuming you meant NO.")

        print("Monster: Roar! Ha-ha!")
        print ("Computer: Uh-oh! Run away! Go, go!")
        print("Human: Aack! I can't survive!")
        print("Human: I am very scared!")
        print("Monster: Roar! Ha-ha!")
