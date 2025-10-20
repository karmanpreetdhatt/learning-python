print("Welcome to Karman's multiplication table generator!")
num = int(input("Enter a number and I will print a table for it: "))

for i in range(50):
    m = i + 1
    product = num * m
    print(f"{num} * {m} = {product}")
