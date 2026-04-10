class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

        #insted using kw[] we can also use get()method the benifit is when user forgot to give any argument than get() method gives None not error like kw[]
        self.speed = kw.get("speed")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

# now we try to give value without give the arguments to funtion
print(my_car.speed)