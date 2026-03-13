def function_1(text):
    return text+text

def function_2(text):
    return text.title()

print(function_2(function_1("hello")))