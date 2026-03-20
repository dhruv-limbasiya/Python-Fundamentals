# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(100)
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#



from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create one object from each blueprint
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        machine_on = False
        print("Shutting down the machine. Goodbye!")

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resources_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)