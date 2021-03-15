# HOrnet RULE
# nested multiplication

#P[n(x)]=a[o] + x(a[1] + x(a[2] + ... + x(a[n-1] + a[n]x)...))


# algorithm 
# pi(x) = a[n-1] + x p[i-1](x)
# i = 1,2,3,...,n
# n = the length of the polinom



# px = 5 + 2x + x^2
# px = 5 + x(2 + x) 
# x = 10

x = 10
a = [5, 2, 1]
n = len(a)
px = a[n - 1]

for i in range(1, n):
    px = a[(n - 1) - i] + (x * px)
print(px)

def hornetRulePol(*args, x):
    n = len(args)
    px = args[n - 1]
    for i in range(1, n):
        px = args[(n - 1) - i] + (x * px)
    return px
# p(x) = 10 + 11X^3 + 12X^2 + 127X^3
# x = 129
print(hornetRulePol(10, 11, 12, 127, x=129))
def countPrime(n):
    count = 0
    for i in range(2, n + 1):
        check = 0
        for j in range(1, n):
            if i % j == 0:
                check += 1
        # print(check)
        # print(i)
        if check == 2:
            #print(i)
            count += 1
    return count
print(countPrime(100))
