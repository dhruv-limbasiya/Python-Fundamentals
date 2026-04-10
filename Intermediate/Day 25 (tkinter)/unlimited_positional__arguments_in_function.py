def add(*args):
    sum=0
    for n in args:
         sum = sum+n
    return sum

print(add(1,2,3,4,5,6,7,8,9))

# *args is a tuple and "*" is important but you can give any name like *a or *arguments