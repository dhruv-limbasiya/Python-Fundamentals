print("Welcome to the profit calculator")

sp = int(input("Enter your Selling Price: "))
cp = int(input("Enter your Cost Price: "))
Basic_profit = sp - cp

tr = int(input("Enter your Total Revenue: "))

np = int(input("Enter you Net Profit: "))
te = int(input("Enter your Total Expenses: "))
Net_profit = tr - te

cogs = int(input("Enter the Cost of goods sold: "))
Gross_profit = tr - cogs

if cp != 0:
    profit_percentage = (Basic_profit / cp) * 100
else:
    profit_percentage = 0

print("Your Basic profit is: ", Basic_profit)
print("Your Total Net Profit is: ", Net_profit)
print("Your Total Gross Profit is: ", Gross_profit)
print("Your profit Percentage is: ", profit_percentage, "%")