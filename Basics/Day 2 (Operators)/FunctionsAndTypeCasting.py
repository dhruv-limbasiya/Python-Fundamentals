print(type("Hello"))

print(type(123))

print(type(12.12))

print(type(True))

################################################

print(int("123") + int("456"))  # 579 because string type cast into int because of int.

print("Number of letters in your name: " + str(len(input("Enter your name:  ")))) #5
# "Number of letters in your name" is a string and "len(input("Enter your name:  ")" this line have integer because of len
# so to concatinate both we should typecast integer to string like this str(len(input("Enter your name:  ")))