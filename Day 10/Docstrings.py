def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name."""
    return f"hello, {f_name} {l_name}".title()


formatted_name = (format_name(input("Enter your first name: "), input("Enter your last name: ")))

print(len(formatted_name))
