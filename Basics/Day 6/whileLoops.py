# 1. Print Numbers 1 to 10

# number = 1
# while number <= 10:
#     print(number)
#     number += 1

# 2. Take an integer n as input and find the sum of numbers from 1 to n.

# num = int(input("Enter the number: "))
# sum = 0
# i = 0
# while i <= num:
#     sum = sum + i
#     i += 1
#
# print(sum)

# 3. Take a number as input and print its multiplication table up to 10.

# table_num = int(input("Enter the number for printing table: "))
# i = 1
# while i <= 10:
#     print(table_num, " * ", i, " = ", table_num * i)
#     i += 1

# 4. Take an integer input and count how many digits it has.

num = int(input("Enter the number: "))
count = 0

while num > 0:
   num //= 10
   count+=1
print(count)