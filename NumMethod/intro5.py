# BINARY TO DECIMAL
def binToDec(bin):
    res = 0
    count = 0
    for i in bin[::-1]:
        res += int(i) * (2**count)
        count += 1
    #return "({}).10".format(res)
    return res
print(binToDec("100100110"))
print(2 ** 1 + 2 ** 2 + 2 ** 5 + 2 ** 8)
# DECIMAL TO BINARY
def decToBin(num):
    bin = ""
    while num > 0:
        if num % 2 == 0:
            bin += "0"
        else:
            bin += "1"
        num = int(num/2)
    #return "({}).2".format(bin[::-1])
    return bin[::-1]
print(decToBin(294))
'''
BINARY : 0 1
DECIMAL : 0 1 2 3 4 5 6 7 8 9
OCTAL : 0 1 2 3 4 5 6 7
'''
def octToDec(oct):
    oct = str(oct)
    res = 0
    count = len(oct)-1
    for ind in oct:
        res += int(ind) * (8)**count
        count -= 1
    return res
print(octToDec(2322))

def binToOct(bin):
    # seperate to group of three
    import math
    idx = len(bin)-1
    groupOfThree = []
    count = 1
    while count <= math.ceil(len(bin)/3):
        #print(idx)
        if len(bin) % 3 == 0:
            groupOfThree.append("{}{}{}".format(bin[idx-2],bin[idx-1],bin[idx]))
            count += 1
            idx -= 3
        else:
            if idx - 2 >= 0:
                groupOfThree.append("{}{}{}".format(bin[idx - 2], bin[idx - 1], bin[idx]))
                count += 1
            else:
                if len(bin) % 3 == 1:
                    temp = "00"
                elif len(bin) % 3 == 2:
                    temp = "0"
                for i in range(len(bin) % 3):
                    temp += bin[idx - i]
                groupOfThree.append(temp)
                count += 1
            idx -= 3 
    oct = ""
    for item in groupOfThree[::-1]:
        temp = 0
        count = 2
        
        for i in item:
            temp += (int(i) * (2 ** count))
            count -= 1
        #print(temp)
        oct += str(temp)
    #return groupOfThree
    return oct
    #print(groupOfThree)
print(binToOct("1111110"))
print(binToOct("11011010"))

# a = [1, 2]
# try:
#     print(a[2])
# except IndexError as e:
#     #print(e)
#     print("OUT OF RANGE NERDS!")
# else:
#     print("OK")
# for i in range(8 % 3):
#     print(i)
def binFracToDecFrac(bin):
    temp = bin.split(".")
    binIntegral = temp[0]
    binFraction = temp[1]
    result = int(binToDec(binIntegral))
    fracTemp = 0
    count = 1
    for ele in binFraction:
        fracTemp += int(ele) * 0.5 ** count
        count += 1
    # print(result)
    # print(fracTemp)
    # print(binFraction)
    return result + fracTemp
# a = "adasda.dsada"
# print(a.split("."))
print("@@@@@@")
print(binFracToDecFrac("110.101"))
print(binFracToDecFrac("101.1101"))
print(binFracToDecFrac("100.011"))
def decFracToBinFrac(dec,precision=10):
    temp = str(dec).split(".")
    tempInte = decToBin(int(temp[0]))
    tempFrac = ""
    frac = float("0." + temp[1])
    for i in range(precision):
        print(frac)
        frac *= 2
        if frac < 1:
            tempFrac += "0"
        elif frac >= 1:
            tempFrac += "1"
            frac -= 1
    return tempInte +"."+ tempFrac
print(decFracToBinFrac(4.47))
print(binFracToDecFrac("100.0111100001"))