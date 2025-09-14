name = input("What is your name: ")
print(f"Hello, {name}!")

gender = input("What is your gender? (M/F)")

if gender == "M":
    print("You are a boy.")
if gender == "F":
    print("You are a girl.")


age = int(input("What is your age: "))


if age < 3:
    print("You are just a small baby!")
elif age < 3 and age > 13:
    print("You are a child.")
elif age < 13 and age > 19:
    print("You are a teenager.")
elif age > 18 and age < 65:
    print("You are an adult.")
elif age > 65:
    print("You are somebody's grandfather/grandmother!")

