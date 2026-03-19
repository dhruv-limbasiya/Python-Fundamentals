def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    return f"hello, {f_name} {l_name}".title()


print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
