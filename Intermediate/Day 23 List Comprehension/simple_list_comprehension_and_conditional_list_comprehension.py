
# in normal way we can add number by 1 like that
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

# in list comprehension we can add number in list by 1 like that
new_list2=[n+1 for n in numbers]
print(new_list2)

# list comprehension also work in string
name = "Dhruv"
name_list = [letter for letter in name]
print(name_list)

#create a list which includes double of range which is 1,2,3,4
double_list = [i*2 for i in range(1,5)]
print(double_list)