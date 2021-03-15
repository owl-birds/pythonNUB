'''
Mkaing pass/token generator
'''
def randomPass(container = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]):
    import random
    temp = []
    # print(container)
    while True:
        try:
            many = int(input("enter how many character that you want in you password : "))
        except:
            print("Invalid Input, Try again")
        else:
            break
    length = len(container) 
    for i in range(many):
        randomIDX = random.randint(0, length-1)
        if type(container[randomIDX]) == type(1):
            temp.append(str(container[randomIDX]))
        else:
            temp.append(container[randomIDX])
    # making pass more complex by adding uppercase letter
    for i in range(0, random.randint(0, many)):
        try:
            idxUpp = random.randint(0, many - 1)
            temp[idxUpp] = temp[idxUpp].upper()
        except ValueError:
            pass
        else:
            pass
    return "".join(temp)
# TEST
# print("".join(["a","r","i","f"]))
# print(randomPass())
# import string
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.)
def func():
    return 1
# def hello():
#     return "HELLO!"
# greet = hello # assign a func into a var
# print(greet())
def hello(name="JACK"):
    #print("hello() function has been executed!")
    def greet():
        return "\tgreet() func inside hello"
    def wellcome():
        return "\twellcome() func inside hello"
    # print(greet())
    # print(wellcome())
    # Return a functiion!
    if name == "JACK":
        return greet
    else:
        return wellcome
print(hello())
print(hello()())
def cool():
    def superCool():
        return "I am very COOL"
    return superCool
###
someFunc = cool() # passing a func into varr
print(someFunc())
###
def newHello():
    return "HI OWL!"
# passing a function as an argument
def other(someDefFunc):
    print("OTHER FUNC")
    print(someDefFunc())
###
other(newHello)
###
def newDecorator(originalFunction):
    def wrapFunc():
        print("Some extra code, before the original function")
        originalFunction()
        print("Some extra code, after the original function")
    return wrapFunc
def funcNeedDecorator():
    print("I want to be decorated!!!!")
decoratedFunc = newDecorator(funcNeedDecorator)
decoratedFunc()
# more slim simple way
@newDecorator
def funcNeedDecorator1():
    print("I want to be decorated!!!!")
funcNeedDecorator1()
# just comment the @decoratorFunc if you dont want your 
# function to be decorated

# web framework for python
# django and flask CHECK THESE OUT 