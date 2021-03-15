#two.py
import one
print("TOP LEVEL IN TWO.PY")
one.myFunc()
if __name__ == "__main__":
    print("TWO.PY IS BEING RUN DIRECTLY")
else:
    print("TWO.py has been impoorted")