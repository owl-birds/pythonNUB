# MAP FUNCT
def squred(n):
    return n ** 2
nums = [1, 2, 3, 4, 8]
for item in map(squred, nums):
    print(item)
def lenEven(myString):
    if len(myString) % 2 == 0:
        return "EVEN"
    else:
        return myString[0]
names = ["arif", "who", "siapa", "kkkk"]
print(list(map(lenEven, names)))
# FILTER FUNCT
def checkEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
def checkEven2(num):
    return num % 2 == 0
print(list(filter(checkEven2, nums)))
print(list(filter(checkEven, nums)))
# LAMBDA EXPRESSION : is usually anonymous function
squred2 = lambda num: num ** 2
print(squred2((5)))

# combining map filter with lambda
print(list(map(lambda num: num ** 2, [3, 2, 4, 6])))
print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6, 7])))
print(list(filter(lambda word: word[0] == "A", ["Arif", "Ikhwan", "Aku", "Apa"])))
print(list(map(lambda word: word[::-1], ["Arif", "Ikhwan", "Aku", "Apa"])))
