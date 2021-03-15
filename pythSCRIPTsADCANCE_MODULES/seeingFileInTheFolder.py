import os
currDir = os.getcwd()
print(currDir)
folderTree = os.walk("extracted_content")
for item in folderTree:
    print(item[0])

def seeTxtFile(osWalk):
    for folders, subFolders, files in osWalk:
        print(folders)
        print(files)
        # for let in folders:
        #     print(let)
seeTxtFile(os.walk("extracted_content"))
def findingPhoneNum(osWalk):
    import re
    phonePattern = r"\d{3}-\d{3}-\d{4}"
    count = 0
    for folder, subFolders, files in osWalk:
        path = "C:\\\\Users\\\\GL503GE\\\\Desktop\\\\notebook J\\\\CSES\\\\advancePythonModules\\\\Excercise\\\\"
        for let in folder:
            if let == "\\":
                path += let
                path += "\\"
            else:
                path += let
        path += "\\\\"
        #print(path)
        for file in files:
            count += 1
            filePath = path + file
            #print(filePath)
            with open(filePath,"r") as myFile:
                sentences = myFile.readlines()
            for sentence in sentences:
                temp = re.search(phonePattern, sentence)
            if type(temp) != type(None):
                #print(count)
                #print(filePath)
                return temp.group()
print(findingPhoneNum(os.walk("extracted_content")))