x = 999
y = "WTF"
def myFunc1():
    global x
    y = 909099
    print("GLOBAL VAR : {}".format(x))
    print("LOCAL : {}".format(y))
myFunc1()