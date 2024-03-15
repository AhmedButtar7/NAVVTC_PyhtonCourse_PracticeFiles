class parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printme(self):
        print(self.firstname, self.lastname)


class Student(parent):
    pass


x = Student('Ahmed', 'Buttar')
x.printme()


# Class Name Animal parent, inherit the birds,mammals , animal contains legs,boolean as feather , milk giving,
class Animal:
    def __init__(self, legs, feathers, milk):
        self.noOfLegs = legs
        self.haveHFather = feathers
        self.milkGiving = milk

    def printMe(self):
        print("Organism has ", self.noOfLegs, " legs \n and have feather: ", self.haveHFather, " \n and is milk giving",
              self.milkGiving)


class Birds(Animal):
    pass


class Mammals(Animal):
    pass


x = Birds(2, True, False)
x.printMe()
y = Mammals(4, False, True)
y.printMe()
