# "x" - Create -
#  will create a file, returns an error if the file exist

# "a" - Append -
#  will create a file if the specified file does not exist

# "w" - Write -
#  will create a file if the specified file does not exist

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

print("reading a txt file")
fileReadTxt = open("part1.txt", "r")
print(fileReadTxt.read())
print("SEEK TO THE BEGINNING")
fileReadTxt.seek(0)
fileReadTxt.readline()
fileReadTxt.close()

fileReadTxt = open("part1.txt", "r")
print(fileReadTxt.read(11))
fileReadTxt.close()

print("dsada")

fileReadTxt = open("part1.txt", "r")
print(fileReadTxt.readline())
print(fileReadTxt.readline())
print(fileReadTxt.readline())
fileReadTxt.close()

print("dsada")

fileReadTxt = open("part1.txt", "r")
for i in fileReadTxt:
    print(i)
fileReadTxt.close()

fileReadTxt = open("part1.txt", "r")
print(fileReadTxt.readlines())
fileReadTxt.close()