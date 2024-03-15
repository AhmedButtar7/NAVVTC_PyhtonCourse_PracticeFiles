# host python website severs search just like Xamp for php and search for python especially
x = "Hello World"
print(len(x))
myTuple = ("apple", "banana", "cherry")
print(len(myTuple))
thisDict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
print(len(thisDict))


# Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    # def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model

    def move(self):
        print("Drive!", self.brand, self.model)


class Boot(Vehicle):
    # def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model

    def move(self):
        print("Sail!", self.brand, self.model)


class Plane(Vehicle):
    # def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model

    def move(self):
        print("Fly!", self.brand, self.model)


car1 = Car("Ford", "Mustang")
boat1 = Boot("Boat 1", "Touring")
plane1 = Plane("Boeing", "754")

for x in (car1, boat1, plane1):
    x.move()


# Python Scope
# Local variable with a variable inside a function and can be accessed in inner function or simply inside a function

def myfun():
    x = 300
    print(x)


myfun()

# Global Function that can be accessed widely throughout the program or class in which it is declared
x = 301


def fun():
    print(x)


fun()
print(x)

import platform

x = dir(platform)
print(x)
