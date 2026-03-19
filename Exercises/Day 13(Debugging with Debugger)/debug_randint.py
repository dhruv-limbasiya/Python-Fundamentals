from random import randint

number = ["1","2","3","4","5","6"]
# random_number = randint(1,6) # it gives error because randint start with 0 and in list their are 5 member not 6 so
random_number = randint(1,5)
print(number[random_number])