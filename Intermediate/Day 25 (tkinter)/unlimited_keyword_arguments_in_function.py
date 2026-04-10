def calculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=9)

# **kwargs is a dictionary, this "**" sign importent but you can give any name like **unlimitedargs, **manyarguments