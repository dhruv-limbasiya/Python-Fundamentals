
#function with print function
def  format_name1(f_name, l_name):
    print(f"Hello, {f_name} {l_name}".title())

f_name1=input("Enter your first name: ")
l_name1=input("Enter your last name: ")

format_name1(f_name1, l_name1)

#function with return keyword
def  format_name(f_name, l_name):
    return f"Hello, {f_name} {l_name}".title()

f_name=input("Enter your first name: ")
l_name=input("Enter your last name: ")

print(format_name(f_name, l_name),"_9")