import math
print(22 / 7)

def sphrereVol(rad):
    return (4 / 3) * (rad ** 3) * math.pi
print(sphrereVol(2))
def isNumIn(num, low, high):
    if num in range(low, high + 1):
        return True
    else:
        return False
def isNumIn2(num, low, high):
    return num in range(low,high+1)
print(isNumIn(8, 9, 10))
print(isNumIn2(8, 9, 10))
def upLow(myString):
    low = 0
    up = 0
    for lett in myString:
        if lett.isupper():
            up += 1
        elif lett.islower():
            low += 1
    print("low : {}\nup : {}".format(low, up))
upLow("Hello Mr. Rogers, how are you this fine Tuesday?")
def isPalindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
def isPalindrome2(word):
    word = word.replace(" ", "")
    return word.lower() == word[::-1].lower()
print("palindrome? "+str(isPalindrome2("hell eh")))
import string
print(string.ascii_lowercase)
def uniqueNums(*args):
    return list(set(args))
print(uniqueNums(1, 1, 1, 1, 1, 3, 4, 5, 5, 5, 6, 6))
def alphabetListReturn():
    import string
    alp = string.ascii_lowercase
    temp = []
    for let in alp:
        temp.append(let)
    return temp
alp = alphabetListReturn()
alp.remove("a")
print(alp)
def isPangram(myString):
    alp = alphabetListReturn()
    for let in myString:
        if len(alp) == 0:
            return True
        if let in alp:
            alp.remove(let)
    return len(alp) == 0
print(isPangram("abcdefghijkylmnopqrstuddvwxz"))
