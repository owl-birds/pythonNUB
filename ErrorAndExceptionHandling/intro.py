def add(a, b):
    print(a + b)
# will be an error if any input ::: string type
try:
    result = 10 + 10
except:
    # run when there are errors in trry block
    print("Hey, you arent adding correctly")
else:
    # run when there are no errors in try bloock
    print("Add went well!")
    print(result)
# still can continue to the next code
add(90, 100)

try:
    f = open("testfile.txt", "r")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("oi,you have an OS error!")
except:
    print("All other errors")
finally:
    print("i always run")

def intInput():
    while True:
        try:
            res = int(input("Please enter a number : "))
        except:
            print("Thaat is not a number!")
            continue
        else:
            print("{} inputted".format(res))
            break
        finally:
            print("End of try/except/finally")
            print("always running")
intInput()