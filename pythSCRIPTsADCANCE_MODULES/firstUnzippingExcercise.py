import shutil
import os
currDir = os.getcwd()
print(currDir)

shutil.unpack_archive("unzip_me_for_instructions.zip", "", "zip")

