from random import randint

flag_list = [
    {"country_name": "India", "flag": "🇮🇳"},
    {"country_name": "United States", "flag": "🇺🇸"},
    {"country_name": "United Kingdom", "flag": "🇬🇧"},
    {"country_name": "Canada", "flag": "🇨🇦"},
    {"country_name": "Germany", "flag": "🇩🇪"},
    {"country_name": "France", "flag": "🇫🇷"},
    {"country_name": "Australia", "flag": "🇦🇺"},
    {"country_name": "Japan", "flag": "🇯🇵"},
    {"country_name": "China", "flag": "🇨🇳"},
    {"country_name": "Brazil", "flag": "🇧🇷"},
    {"country_name": "Italy", "flag": "🇮🇹"},
    {"country_name": "Russia", "flag": "🇷🇺"},
    {"country_name": "South Korea", "flag": "🇰🇷"},
    {"country_name": "Mexico", "flag": "🇲🇽"},
    {"country_name": "Spain", "flag": "🇪🇸"},
    {"country_name": "Netherlands", "flag": "🇳🇱"},
    {"country_name": "Sweden", "flag": "🇸🇪"},
    {"country_name": "Norway", "flag": "🇳🇴"},
    {"country_name": "Switzerland", "flag": "🇨🇭"},
    {"country_name": "New Zealand", "flag": "🇳🇿"},
    {"country_name": "South Africa", "flag": "🇿🇦"},
    {"country_name": "Argentina", "flag": "🇦🇷"},
    {"country_name": "Turkey", "flag": "🇹🇷"},
    {"country_name": "Indonesia", "flag": "🇮🇩"},
    {"country_name": "Malaysia", "flag": "🇲🇾"},
    {"country_name": "Philippines", "flag": "🇵🇭"},
    {"country_name": "Thailand", "flag": "🇹🇭"},
    {"country_name": "Vietnam", "flag": "🇻🇳"},
    {"country_name": "Saudi Arabia", "flag": "🇸🇦"},
    {"country_name": "Egypt", "flag": "🇪🇬"},
]
answer = "Y"

correct_answers = 0
wrong_answers = 0

while answer.upper() == "Y":
    # Generate a random number from 0 to length of flag list
    random_num = randint(0, len(flag_list))

    flag = flag_list[random_num]["flag"]
    country_name = flag_list[random_num]["country_name"]

    country = input(f"Guess the country having this flag {flag} ")

    if country.upper() == country_name.upper():
        correct_answers += 1
        print("You are right 🙂")

    else:
        wrong_answers += 1
        print("You are wrong ☹️")
        print(f"The answer was {country_name} 😎")

    answer = input("Do you want to play again? (Y/N): ")

print(f"Your score is: {correct_answers}/{correct_answers+wrong_answers} ")
print("Bye, hope you enjoyed Karmanpreet's flag guessing game! 👋👋")
