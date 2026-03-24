class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Details of Employee: {self.id} is {self.name} from employee class")


class Programmer(Employee):
    def showLanguage(self):
        print("Defult Language is Python. from programmer class")

e = Employee("Any",123)
e.showDetails()


print("\n")

e2=Programmer("Anybody",456)
e2.showDetails() # this line works because we inherit employee class in programmer class
e2.showLanguage()