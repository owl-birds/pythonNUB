'''
squares generators
'''
def genSquares(n):
    for i in range(n):
        yield i ** 2
print(list(genSquares(10)))
'''
random num between 2 nums
'''
def randNums(low, high, n):
    import random
    for i in range(n):
        yield random.randint(low, high)
print(list(randNums(1, 10, 12)))
'''
iterator
'''
def iteratorDemo(inString):
    temp = iter(inString)
    for i in range(len(inString)):
        print(next(temp))
iteratorDemo("ARIF")
'''
crack string into pieces
'''
def stringCrack(myString):
    for letter in myString:
        yield letter
print(list(stringCrack("ARIF IKHWAN")))
'''
fibbonaci
'''
def genFibbo(n):
    num1 = 1
    num2 = 1
    for i in range(n):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2 
print(list(genFibbo(10)))
'''
generator comprehension
'''
myList = [1, 2, 3, 4, 5]
gencomp = (item for item in myList if item > 3)
for item in gencomp:
    print(item)