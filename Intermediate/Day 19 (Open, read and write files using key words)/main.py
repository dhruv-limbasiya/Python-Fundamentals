# always close the file when open:
# file = open("my_file.txt")
#
# contents = file.read()
# print(contents)
#
# file.close()


# another way to open file with this type of opening we not need to close file manually:
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


#write in the file:
with open("my_file.txt",mode="a") as file:# "w" stands for write, "a" stands for append
    file.write("\nNew text.")
    file.write("\nNew text....")


#even if file does ont exist in folder "w" mode create file and write the txt. this feature works in only write mode.
with open("new_file.txt",mode="w") as file:# "w" stands for write, "a" stands for append
    file.write("\nNew text....")