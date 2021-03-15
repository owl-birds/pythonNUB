class NameOfClass():
    # initiating the attribute of the class
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    def some_method(self):
        print(self.param1)
        print(self.param2)
    
#SIMPLPE CLASS EXAMPLE
class Cat():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF CLASS
    species = "mammal"


    #Constructor of the CLass
    def __init__(self, breed, myColor, name):
        #Attribute
        # We take the arguments then we assign it in 
        # self.attributeName
        # ATtribute can be anything String, int, float, boolean etc

        #Expect String
        self.breed = breed
        self.color = myColor
        self.name = name
    # METHODS 
    def desc(self,number):
        print("my cat description")
        print("my cat name : {}".format(self.name))
        print("my cat breed : {}".format(self.breed))
        print("my car color : {}".format(self.color))
        print("number : {}".format(number))

myCat = Cat(breed="Angora", myColor="Orange", name="Oreo")
print(myCat.name+"-"+myCat.breed + "-" + myCat.color)
print(myCat.species)
myCat.desc(number=999)

class Circle():
    # CLass OBJECT ATTRIBUTE
    from math import pi
    circlePi = pi

    # constructor
    def __init__(self, radius = 1): #default rad = 1 can overwrite
        self.radius = radius
        self.area = radius ** 2 * Circle.circlePi  #can be defined like tthis
        # reference to class obj attr
    #METHOD
    def circumference(self):
        return Circle.circlePi * self.radius * 2
circle1 = Circle(30)
print("Circumference: " + str(circle1.circumference()) + " area: " + str(circle1.area))
