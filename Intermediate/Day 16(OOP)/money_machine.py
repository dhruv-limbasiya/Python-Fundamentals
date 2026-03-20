class MoneyMachine:
    # handles all the money / payments
    CURRENCY = "₹"
    MONEY_VALUES = {
        "10": 10,
        "20": 20,
        "50": 50,
        "100": 100
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        # Showshow much money the mchine has earned
        print(f"Money: {self.CURRENCY}{self.profit}")

    def proccess_coins(self):
        # ask user to insert money and add them up
        print("Please insert Money.")
        for money in self.MONEY_VALUES:
            self.money_received += int(input(f"How many {self.CURRENCY}{money}?: ")) * self.MONEY_VALUES[money]
        return self.money_received

    def make_payment(self, cost):
        # check if user paid enough
        self.proccess_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
