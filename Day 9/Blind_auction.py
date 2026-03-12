gavel_logo = r'''
             _____________
            /             \
           /               \
          (_________________)
           |"""""""""""""""|_.-._,.-----------.,_.-._
           |               | | |               | |  '-.
           |               |_| |_             _| |_..-'
           |_______________| '-' `'---------'` '-'
           (""""""""""""""")
           /_______________\
           `'-------------'`
         .-------------------.
        /_____________________\
'''

print(gavel_logo)
print("Welcome to the secret auction program.")

bidders = {}

say = "yes"

while say == "yes":
    name = input("What is your name: ")
    bid = int(input("What's your Bid: $"))

    bidders[name] = bid

    any_bidders = input("Are there any other bidders? Type 'yes' OR 'no': ").lower()

    if any_bidders == "no":
        say = "no"
    else:
        print("\n" * 100)

winner = ""
highest_bid = 0

print("\n" * 100)
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        winner = key

print(f"The winner is {winner} with bid ${highest_bid}")