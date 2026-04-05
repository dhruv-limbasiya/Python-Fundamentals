# this is fileNotFoundError:
# with open("a_file.tx") as file:
#     file.read()

# keyError
# a_dict = {"key" : "value"}
# vlaue = a_dict["not_exist"]

#IndexError
# fruit_list = ["Apple", "Banana" , "Pear"]
# fruit = [fruit_list[3]]

#TypeError
# text = "avx"
# print(text + 5)

# now this is the solution to catch error
try:
    file = open("a_file.txt")
    # this is second error
    a_dict = {"key": "value"}
    print(a_dict["asd"])

except FileNotFoundError:
    # print("Ther was an error")
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

# when above try block not have ecxeption than the else block works
else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")