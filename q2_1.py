class Car():
    '''A class to represent a car'''
    def __init__(self, make = "", model = "", year = ""):
        self.make = make
        self.model = model
        self.year = year
        self.my_class = "Car"

    def __str__(self):
        class_name = type(self).__name__
        return f"<{class_name} {self.make} {self.model} {self.year}>"

outback = Car("Subaru", "Outback", "1999")
test_car = Car('Ford', "taurus")

print(outback.year)
#prints 1999
print(outback)
# prints something like:
# <Car 1999 Subaru Outback>
