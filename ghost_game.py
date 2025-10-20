# Ghost Game
from random import randint

print(" Welcome to Karmanpreet's Ghost Game!")
print("----------")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print("Three doors ahead...")
    print("A ghost behind one...")
    print("Which door do you want to open?")
    door = input(
        """1, 2 or 3?
    Type your answer here:  """
    )
    door_num = int(door)
    if door_num == ghost_door:
        print("GHOST! GHOST! Aaah! 😱😱😱")
        feeling_brave = False
    else:
        print("No ghost! THANK GOD! 🥲")
        print("You are lucky! ☺️☺️")
print("Run! Quick, quick! Oh, quuuuuuuuiiiiiiiiiccckk!")
print(f"Game over! Your score is: {score}")