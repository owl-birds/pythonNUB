with open("part1.txt") as myNewFile:
    contents = myNewFile.read()
print(contents)
print(type(contents))

myFile = open("C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES\\IO\\part1.txt", "r")
print(myFile.read())
myFile.close()

with open("part1.txt", mode="a") as myFile:
    myFile.write("This line 4\n")

with open("part1.txt", mode="r") as myFile:
    contents = myFile.read()
print(contents)