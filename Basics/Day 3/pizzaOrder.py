print("WelCome to Python pizza Deliveries. ")

pepperoni = 0
extra_cheese = 0
total_bill = 0

size = input("what size pizza do you want? S, M, L: ")

if size == "s" or size == "S":
    total_bill += 15
    pepp = input("Do you want pepperoni on your small pizza? type 'y' for yes or 'n' for no: ")
    if pepp == "y" or pepp == "Y":
        total_bill += 2
    extra_cheese = input("Do you want extra cheese? type 'y' for yes or 'n' for no: ")
    if extra_cheese == "y" or extra_cheese == "Y":
        total_bill += 1
    print(f"Your total bill is {total_bill}$")

elif size == "m" or size == "M":
    total_bill += 20
    pepp = input("Do you want pepperoni on your Medium pizza? type 'y' for yes or 'n' for no: ")
    if pepp == "y" or pepp == "Y":
        total_bill += 3
    extra_cheese = input("Do you want extra cheese? type 'y' for yes or 'n' for no: ")
    if extra_cheese == "y" or extra_cheese == "Y":
        total_bill += 1
    print(f"Your total bill is {total_bill}$")

elif size == "l" or size == "L":
    total_bill += 20
    pepp = input("Do you want pepperoni on your Large pizza? type 'y' for yes or 'n' for no: ")
    if pepp == "y" or pepp == "Y":
        total_bill += 3
    extra_cheese = input("Do you want extra cheese? type 'y' for yes or 'n' for no: ")
    if extra_cheese == "y" or extra_cheese == "Y":
        total_bill += 1
    print(f"Your total bill is {total_bill}$")

else:
    print("Not Valid Letter")