#one.py
#print("helo")
# declaring some var, methods, func, class etc
def myFunc():
    print("one.py NANI __name__ == __main__")
#checking if its is run directly
def function1():
    pass

# logic where you executing things
if __name__ == "__main__":
    # RUN THE SCRIPT
    myFunc()
    function1()
    print("one.py is being run directly")
else:
    print("one.py has been imported")