def greet():
    print("Hello!")
    print("How you do!")
    print("Isn't the wather nice?")

greet()

print("\n")
#function with string parameter

def greet_with_name(name):
    print(f"Hello! {name}")
    print("How do you do!", name)

name=input("Enter your name: ")
greet_with_name(name)

print("\n")

#function with string two parameter

def greet_with(name,location):
    print(f"Hello! {name}")
    print(f"{location} is a good city.")

name_for_greeth_with = input("Enter your name: ")
location_for_greeth_with = input("Enter your location(city): ")
greet_with(name_for_greeth_with,location_for_greeth_with)

print("\n")
#function with integer parameter

def sum(a,b):
    sum = a+b
    print(sum)

ele1=int(input("Enter first number to add: "))
ele2=int(input("Enter second number to add: "))
sum(ele1, ele2)