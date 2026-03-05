print("Welcome to the Mall")
height = int(input("Enter your height: "))

total_bill = 0

if height >= 120:
    print("you can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("You should be pay 5$.")
        total_bill = 5
    elif age <= 18:
        print("You should be pay 7$.")
        total_bill = 7
    elif age >= 45 and age <= 55: # you can write also like that 45<= age <=55
        print("you can ride for free.")
        total_bill = 0
    else:
        total_bill = 12
        print("You should be pay 12$.")


    wants_photo = input("You want photo with ride..? Type 'y' for yes and 'n for no : ")

    if wants_photo == "y":
        total_bill += 3

    print(f"Your total bill is {total_bill}$")
else:
    print("You can not ride the rollercoaster.")
