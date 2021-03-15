from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os
from PIL import Image

# VID SOURCE
sourceDir = os.path.join(SAMPLE_OUTPUTS, "cutingVideo\\tempCuts")

# OUTPUT DIRECTORY
outputDir = os.path.join(SAMPLE_OUTPUTS, "PPLcombineVid")
# MAKE DIR
os.makedirs(outputDir, exist_ok=True)

# listFile
fNames = []
for folder, subfolders, files in os.walk(sourceDir):
    # print(files)
    for fname in files:
        tempPath = os.path.join(sourceDir, fname)
        fNames.append(tempPath)
# print(fNames)

videoClips = []
for path in fNames:
    tempClip = VideoFileClip(path)
    videoClips.append(tempClip)
# print(videoClips)
def combineVid(vidClips, outputDir, fileName = "combinedVid.mp4"):
    idx = 1
    tempClip = vidClips[idx]
    while idx < len(vidClips):
        tempClip = concatenate_videoclips([tempClip, vidClips[idx]])
        idx += 1
    outputPath = os.path.join(outputDir, fileName)
    tempClip.write_videofile(outputPath)
combineVid(videoClips, outputDir)
