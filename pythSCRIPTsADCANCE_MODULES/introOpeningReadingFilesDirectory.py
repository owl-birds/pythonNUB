'''
Collections MOdule
'''
from collections import Counter
myNums = [1, 1, 1, 11, 1, 1, 1, 1, 2, 2, 2, 22, 2, 2, 22, 3, 3]
print(Counter(myNums))
print(Counter("AAAAAABBBaaaCCCccc".lower()))
sentence1 = "Sentence is a collection of words that have a certain Meaning"
print(Counter(sentence1.lower().split()))
letters = "aaaaabcascdadasdafd"
c = Counter(letters)
print(c)
# returning 2 most common
print(c.most_common())
print(c.most_common(2))
print(sum(c.values()))
print(len(letters))
print(list(c))
print(c.items())
print(c.keys())
print(c.values())
'''
default dictionaries
'''
from collections import defaultdict
d = {"a": 100}
print(d["a"])
try:
    print(d["Wrong key"])
except KeyError:
    print("invalid Key")
d = defaultdict(lambda: 0)
d["a"] = 999
print(d["a"])
print(d["unknown_key"])
print(d)
print(d.items())
'''
named tuple
'''
myTuple1 = (1, 2, 3, 4)
print(myTuple1[0])
from collections import namedtuple
Dog = namedtuple("Dog", ["age", "breed", "name"])
print(Dog)
print(type(Dog))
sam = Dog(age=100, breed="mixed", name="Sam")
print(sam)
print(type(sam))
'''

'''
#finding the current directory
import os
print(os.getcwd())
print(type(os.getcwd))
print(os.getcwdb())
print(type(os.getcwdb))
# myFile = open("practice.txt", "w")
# myFile.write("HELLO, THIS IS TEST STRING\n")
# myFile.close()
# myFile = open("practice.txt", "a")
# myFile.write("HELLO, THIS IS TEST STRING\n")
# myFile.close()

# listing items in directories
print(os.listdir())
#print(os.listdir("C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES"))

# moving file in dir
import shutil

# move it into CSES DIR
# firts you have to remember thaht the file that
# you want to move is the same dir with the python script
##shutil.move("practice.txt", "C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES")

# move it back again
##shutil.move("practice2.txt", "C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES\\advancePythonModules")

#shutil.move("path/file.file", "Path to file")

'''
removing with os
os.unlink(path) : deletes a file at the path you are providing
os.rmdir(path) : deletes an empty foleder at the path you
                 are providing
shutil.rmtree(path) : remove all files and folder contained in
                      the path (BE CAREFUl)
ALL THE METHOD ABOVE CANT BE REVERSED 
DONT MAKE MISTAKE OK
YOU cANT RECOVER THE FILE
BUT INSTEAD WE WILL USE send2trash module, A safer alternative 
That sends deleted files to the trash bin instead of permanent
removal
'''
print(os.listdir("C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES\\advancePythonModules"))
import send2trash

# this will sending file into recycle BIN
#send2trash.send2trash("C:\\Users\\GL503GE\\Desktop\\notebook J\\CSES\\advancePythonModules\\practice2.txt")

'''
'''
# Tuple Unpacking
for folder , sub_folders , files in os.walk("Example_Top_Level"): 
    print("Currently looking at folder: " + folder)
    print(type(folder)==type("aa"))
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')

# os.walk("Folder NAme") : making tree based on the folder 
# that you want, so you can look directory within directory 
# with all of their files  
for item in os.walk("Example_Top_Level"):
    print(item)
    