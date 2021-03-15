# GENERATORS : EFFICIENT IN MEMMOORY
# ex : range()
def createCubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result
print(createCubes(10))
# CREATING SIMPLE GENERATORS
def createCubes2(n):
    for x in range(n):
        yield x ** 3
print(createCubes2(10))
for i in createCubes2(10):
    print(i)
print(list(createCubes2(10)))
'''
making generator funtion for fibbonacii num
'''
def genFibbonaci(n):
    num1 = 1
    num2 = 1
    for i in range(n):
        yield num1
        num1,num2 = num2, num1+num2
print(list(genFibbonaci(10)))
def simpleGen():
    for i in range(3):
        yield i
g = simpleGen()
print(g)
print(next(g))
print(next(g))
print(next(g))
s_iter = (iter("ARIF"))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(list(s_iter))