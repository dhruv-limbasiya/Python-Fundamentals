class MenuItem:
    # this is blueprint of one drink
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=250),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=300),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=350),
        ]

    def get_items(self):
        # returns ll drink name like: "latte,...."
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        #searchs for a drink by name, returns it if found
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that drink is not available.")
        return None

