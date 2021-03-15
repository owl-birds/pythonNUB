# y = 4 - x^2
# bb = -1 ba = 1

bb = -1
ba = 1
divide = 10000
areaBelowFunc = 0

while bb <= ba:
    itr = 2 / divide
    fTing = 4 - (bb + itr)** 2
    tempArea = itr * fTing
    areaBelowFunc += tempArea
    bb += itr
print(areaBelowFunc)
print(22 / 3)
