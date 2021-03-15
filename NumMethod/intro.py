# f(x) = x^2-6x+8 = 0
# 3 - 6 (batas bawah dan batas atas)
# error yg di request = 0.0005

bb = 3
ba = 6
eReq = 0.0005
e = 999999999

while e > eReq:
    nt = (bb + ba) / 2
    fbb = bb ** 2 - 6 * bb + 8
    fnt = nt ** 2 - 6 * nt + 8
    if fnt > 0:
        ba = nt
    else:
        bb = nt
    #print(nt)
    e = abs(fnt - 0)
print(nt)
def hornetRulePol(listPar, x):
    n = len(listPar)
    px = listPar[n - 1]
    for i in range(1, n):
        px = listPar[(n - 1) - i] + (x * px)
    return px
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
print(bisectionMethod([8, -6, 1], 6, 3, 0.0005))
print(hornetRulePol([8, -6, 1],4))