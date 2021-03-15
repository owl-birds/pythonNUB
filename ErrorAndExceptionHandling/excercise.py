#1
try:
    for i in ["1", "a", "b", "c"]:
        print(i ** 2)
except TypeError as e:
    print("There is an error : {}".format(e))
else:
    print("YEAH")
#2
try:
    x = 100
    y = 0
    z = x / y
except ZeroDivisionError as e:
    print("error : {}".format(e))
else:
    print("SUCCESS")
finally:
    print("ALL DONE")
#3
def ask():
    while True:
        try:
            res = int(input("Enter an integer : "))
        except:
            print("ERROR OCCURED, please enter an integer")
        else:
            print("your squared number: {}".format(res ** 2))
            break
        finally:
            print("SUCCESS")
ask()

