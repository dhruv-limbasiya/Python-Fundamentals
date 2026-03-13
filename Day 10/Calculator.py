# we can store a function in variable like this
# container=add
# print(container(2,4))
logo = """   _____________________
            |  _________________  |
            | |              0. | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |
            | |___|___|___| |___| |
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|
"""

print(logo)

def add(a1, a2):
    return a1 + a2

def subtract(s1, s2):
    return s1 - s2

def multiply(m1, m2):
    return m1 * m2

def divide(d1, d2):
    return d1 / d2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number: "))

while True:

    for key in operations:
        print(key)

    operation = input("Pick an operation: ")
    num2 = int(input("What's the next number: "))

    ans = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {ans}")

    con_or_new = input(
        f"Type 'y' to continue calculating with {ans} or type 'n' to start a new calculation: "
    ).lower()

    if con_or_new == "y":
        num1 = ans

    elif con_or_new == "n":
        print("\n" * 100)
        num1 = int(input("What's the first number: "))

    else:
        print("Provide valid input")