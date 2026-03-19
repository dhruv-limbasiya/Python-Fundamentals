import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@','#','$','%','^','&','*','(',')','?']


print("Welcom to python password Generator")
nr_letters = int(input("How Many letters would you like in your password: \n"))
nr_numbers = int(input("How Many numbers would you like: \n"))
nr_symbols = int(input("How Many symbols would you like: \n"))


password=""
#Easy level

# for i in range(0, nr_letters+1):
#     password+=random.choice(letters)
#
# for i in range(0, nr_numbers):
#     password+=random.choice(numbers)
#
# for i in range(0, nr_symbols):
#     password+=random.choice(symbols)
#
# print("Your Password:", password)


# hard level
password_list=[]


for i in range(0, nr_letters+1):
    password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# print("Your Password:", password_list)
random.shuffle(password_list)
# print("Your Password: ", password_list)

for i in password_list:
    password+=i

print(f"Your Password is: {password}")


# for i in range(97,123):
#     print(f"'{chr(i)}'",end=', ')

# for i in range(1, 10):
#     print(f"'{i}'",end=", ")