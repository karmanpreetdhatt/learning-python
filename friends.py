from random import randint

friend_list = [
    "Riyan",
    "Nyra",
    "Lakshay",
    "Nurin",
    "Prabhdeep",
    "Paarth"
    "Aarish"
    "Ruhi"
]

random_num = randint(0, len(friend_list) - 1)
print(friend_list[random_num])
print("You made a tag! - #friendshine")