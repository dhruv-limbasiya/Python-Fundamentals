try:
    age = int(input("Enter Your age: "))
    if age > 18 :
        print(f"You can drive because your age is {age}")
    else:
        print("You can not drive")
except ValueError:
    print("You have type invalid number. try again")
    age = int(input("Enter Your age: "))