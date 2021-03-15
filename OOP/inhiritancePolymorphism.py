#INHERITANCE
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def whoAmI(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
#myAnimal = Animal()

# dog inheriting from animal, many similarities
# dog can use anythinf in ANIMAL CLASS
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name
        print("Dog Created")
    #overwriting fromm parent class
    def whoAmI(self):
        print("i am a dog")
    #new method
    def speak(self):
        return self.name + " says WOOF WOOF"
myDog = Dog("Jack")
myDog.eat()
myDog.whoAmI()
#POLYMORPHISM
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow mewo"
oreo = Cat("Oreo")
print(oreo.speak())
print(myDog.speak())
# dog and cat have the same method speak
# but its unique to that particular class

for pet in [myDog, oreo]:
    print(type(pet))
    print(pet.speak())

# ABSTRACT 
class Animal2():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
myAnimal2 = Animal2("WHO")
#myAnimal2.speak()
class Dog2(Animal2):
    def speak(self):
        return self.name + " SAYS WOOF WOOF"
class Cat2(Animal2):
    def speak(self):
        return self.name + " SAYS MEOW MEOW"
cat2 = Cat2("Black")
dog2 = Dog2("White")
print(cat2.speak())
print(dog2.speak())