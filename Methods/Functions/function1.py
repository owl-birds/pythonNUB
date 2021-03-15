# name = "arif"
# print(list(name))
from random import shuffle


def palindromeWordCheckTF(stringTemp):
    temp = list(stringTemp.lower())
    reversedWord = list(stringTemp.lower())
    reversedWord.reverse()
    count = 0
    #print(reversedWord)
    #print(temp)
    for i in range(len(temp)):
        if temp[i] == reversedWord[i]:
            count += 1
        else:
            return False
    if count == len(temp):
        return True
print(palindromeWordCheckTF("ariffir"))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))
#Tuple unpacking
workHours = [("Arif", 90), ("Ikhwan", 120), ("Hendra", 111)]
def employeeCheck(workHours):
    currentMax = 0
    employeeOfMonth = ""
    for name, workHour in workHours:
        if workHour > currentMax:
            currentMax = workHour
            employeeOfMonth = name
    return (employeeOfMonth, currentMax)
print(employeeCheck(workHours))

def threeCupMontee():
    threeCups = ["", "o", ""]
    shuffle(threeCups)
    #print(threeCups)
    print("Three Cup Montee Game")
    print("choose from cup 1,2, and 3")
    guess = int(input("Enter Your Guess :"))
    if guess == (threeCups.index("o") + 1):
        print("You are right!, CONGRATULATION!")
    else:
        print("WRONG! the coin is in {}-th cup".format(threeCups.index("o") + 1))
#threeCupMontee()

# *args **kwargs
def myFunc(a, b):
    # returns 5% of the sum of a and b
    return (a + b) * 0.05
print(myFunc(40, 60))
# woork with many parameters
def myFunc2(*args):
    print(args)
    return sum(args) * 0.05
print(myFunc2(40, 60, 100, 1, 34))
# *something **something
# convention thing *args **kwargs
# *args  ::: TUPLE
# **kwargs ::: dictionary
def sum(*numbers):
    temp = 0
    for i in numbers:
        temp += i
    return temp
print(sum(90,20,20))
def myFunc3(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I dont like any of this")
myFunc3(fruit="Apple", gun="AK47", veggie="TOMATO")
# order MATTER
def myFunc4(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[1], kwargs["drink"]))
myFunc4(20, 999, 90, drink="orange Juice", food="Fried Chicken")

# even collector
def evenCollect(*args):
    li = []
    for i in args:
        if i % 2 == 0:
            li.append(i)
    return li
print(evenCollect(1, 2, 3, 43, 2, 53))

# even upper odd lower
def evOdUpLow(aString):
    temp = ""
    count = 1
    for i in aString.lower():
        if count % 2 == 0:
            temp += i.upper()
            count += 1
        else:
            temp += i
            count += 1
    return temp
print(evOdUpLow("Anthropomorphism"))
def lesserOrGreater(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        if a < b:
            return a
        else:
            return b
    else:
        if a < b:
            return b
        else:
            return a
print(str(lesserOrGreater(2, 4)) + " " + str(lesserOrGreater(2, 5)))
def animalCrackers(text):
    temp = text.split()
    if temp[0][0].lower() == temp[1][0].lower():
        return True
    else:
        return False
print(animalCrackers("alevel, Lever"))
def makesTwenty(a, b):
    if (sum(a, b) == 20) or a == 20 or b == 20:
        return True
    else:
        return False
print(makesTwenty(22,10))
def firstFourthUpper(word):
    temp = ""
    idx = 0
    while idx < len(word):
        if idx == 0 or idx == 3:
            temp += word[idx].upper()
        else:
            temp += word[idx]
        idx += 1
    return temp
print(firstFourthUpper("macdonald"))
def reverseWordINSentence(sentence):
    temp = sentence.split()
    temp.reverse()
    tempSent = ""
    for word in temp:
        tempSent += word + " "
    #return tempSent
    return " ".join(temp)
print(reverseWordINSentence("I am home"))
def almostThere(n):
    if (n >= (100 - 10) and n <= (100 + 10)) or (n >= (200 - 10) and n <= (200 + 10)):
        return True
    else:
        return False
print(almostThere(210)) 
def has33(nums):
    if 3 in nums:
        idx = 0
        while idx < len(nums):
            if idx == (len(nums) - 1):
                return False
            elif nums[idx] == 3 and nums[idx + 1] == 3:
                return True
            idx += 1
        return False
    else:
        return False
print(has33([1,3,1,3,1,3,1,3]))
def multipltLetter(word):
    temp = ""
    for i in word:
        for j in range(0, 3):
            temp += i
    return temp
print(multipltLetter("arif"))
def blackJack(*args):
    total = 0
    for i in args:
        total += i
    if total <= 21:
        return total
    elif (total > 21) and (11 in args):
        return (total - 10)
    else:
        return "BUST"
print(blackJack(9, 9, 11))
def range6to9Pass(*args):
    total = 0
    if len(args) == 0:
        return 0
    else:
        for i in args:
            if i in range(6, 10):
                pass
            else:
                total += i
    return total
print(range6to9Pass(4, 5, 6, 7, 8, 9))
def hindFinder007(*args):
    idx = 0
    while idx < len(args):
        if idx == (len(args) - 2):
            return False
        elif args[idx] == 0 and args[idx + 1] == 0 and args[idx + 2] == 7:
            return True
        idx += 1
print(hindFinder007(1, 2, 3, 0, 0, 7, 4))
def spyGames(*args):
    idx = 0
    count = 0
    tempList = []
    while idx < len(args):
        if args[idx] == 0 or args[idx] == 7:
            tempList.append(args[idx])
        idx += 1
    if len(tempList) == 0:
        return False
    else:
        idx = 0
        while idx < len(tempList):
            if idx == (len(tempList) - 2):
                return False
            elif tempList[idx] == 0 and tempList[idx + 1] == 0 and tempList[idx + 2] == 7:
                return True
            idx += 1
print(spyGames(1, 2, 3, 0, 3213, 321, 321, 90, 0, 1, 7))
