from maths import addition, subtraction, division, multiplication, square, square_root

answer = "Y"

while answer.upper() == "Y":

    choice = int(
        input(
            """Please select what you would like to do: 
1 for addition
2 for subtraction
3 for multiplication
4 for division
5 for square
6 for square root

Please enter your choice: """
        )
    )

    if choice == 1:
        print("You have chosen addition")
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))

        result = addition(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == 2:
        print("You hace chosen subtraciton.")
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))

        result = subtraction(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == 3:
        print("You have chosen multiplication.")
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))

        result = multiplication(num1, num2)
        print(f"{num1} × {num2} = {result}")

    elif choice == 4:
        print("You have chosen division.")
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))

        result = division(num1, num2)
        print(f"{num1} ÷ {num2} = {result}")

    elif choice == 5:
        print("You have chosen square.")
        num = int(input("Enter any number: "))

        result = square(num)
        print(f"The square of {num} is {result}")

    elif choice == 6:
        print("You have chosen square root.")
        num = int(input("Enter any number: "))

        result = square_root(num)
        print(f"√{num} = {result}")

    else:
        print("You have entered an incorrect choice.")

    answer = input("Do you want to continue? (Y/N): ")

print("Bye bye, thank you for using Karman's calculator!")
