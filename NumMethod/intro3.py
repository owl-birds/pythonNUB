# f(x) = 23.4X^4 - 1.25X^3 + 120X^2 + 15X - 100 = 0
# bb = -2 ba = 0
# eReq = 0.00001

bb = -2
ba = 0
eReq = 0.00001
itr = 0.000001111011111001
fnt = (bb ** 4) * 23.4 - (bb ** 3) * 1.25 + (bb ** 2) * 120 + (bb) * 15 - 100
print(fnt)
# e = 99999999
# count = 0
# while bb < ba:
#     fnt = (bb ** 4) * 23.4 - (bb ** 3) * 1.25 + (bb ** 2) * 120 + (bb) * 15 - 100
#     count += 1
#     #print(fnt)
#     if e < abs(fnt - 0):
#         print("Error : "+str(e))
#         print("x : "+str(temp))
#         print("y : "+str(tempFnt))
#         print("iteration : {}".format(count))
#         break
#     else:
#         e = abs(fnt - 0)
#         temp = bb
#         tempFnt = fnt    
#         bb += itr
# print(temp)

def hornetRulePol(listPar, x):
    n = len(listPar)
    px = listPar[n - 1]
    for i in range(1, n):
        px = listPar[(n - 1) - i] + (x * px)
    return px
# f(x) = 23.4X^4 - 1.25X^3 + 120X^2 + 15X - 100 = 0
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-2))
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=0))
# ba and bb beda tanda :: berarti ada suatu nilai a antara
# ba dgn bb yang nilai f(a) = 0
def bisectionMethod(listPar, ba, bb, eReq):
    e = 99999999
    fnt = 0
    while e > eReq:
        nt = (bb + ba) / 2
        fnt = hornetRulePol(listPar, nt)
        if fnt > 0:
            ba = nt
        else:
            bb = nt
        e = abs(fnt - 0)
    return nt
#print(bisectionMethod([-100, 15, 120, -1.25, 23.4],0,-2,0.00001))
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1))
print((-1-2)/2)
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1.5))
print((-2 - 1.5) / 2)
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1.75))
print((-2 - 1.75) / 2)
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1.875))
print((-2 - 1.875) / 2)
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1.9375))
print((-2 - 1.9375)/2)
print(hornetRulePol([-100, 15, 120, -1.25, 23.4], x=-1.96875))
