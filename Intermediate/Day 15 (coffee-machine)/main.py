menu ={
    "latte" :{
        "ingredients" :{
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 250,
    },
    "cappuccino" :{
        "ingredients" :{
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 200,
    },
}

profit = 0
resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def is_resoruce_sufficient(order_ingredients):
    """returns ture when order can be made, flase if ingredients are insufficint."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True



def process_coins():
    """returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many ₹10: "))*10
    total += int(input("How many ₹20: "))*20
    total += int(input("How many ₹50: "))*50
    total += int(input("How many ₹100: "))*100
    return total


def is_transaction_successful(money_received, drink_cost):
    """returns true when the payment is accepted, or false if monay if insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost

        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    """deduct the requaired ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵")


is_on = True
while is_on:
    choice = input("What wauld you like? (latte / cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = menu[choice]
        if is_resoruce_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
