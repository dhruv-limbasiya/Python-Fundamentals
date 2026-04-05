# try:
#     file = open("a_file.txt")
#     # this is second error
#     a_dict = {"key": "value"}
#     print(a_dict["asd"])
#
# except FileNotFoundError:
#     # print("Ther was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
#
# # when above try block not have ecxeption than the else block works
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     # raise keyword help to raise our own exception
#     # when we write raise keyword and raise any type of error it show every time when code runs because finally block runs always
#
#     raise TypeError("This is an error that i made up.")

height = float(input("Height in meter: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)