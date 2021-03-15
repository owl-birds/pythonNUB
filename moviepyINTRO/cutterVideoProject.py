from conf import SAMPLE_OUTPUTS, SAMPLE_INPUTS
from moviepy.editor import *
import os
from math import ceil

# SOURCE PATH
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")

# MAKING DIRECTORY
cutsDir = os.path.join(SAMPLE_OUTPUTS, "cutingVideo")
cutsDir = os.path.join(cutsDir, "tempCuts")
os.makedirs(cutsDir,exist_ok=True)

# deafult OUTPUT PATH
fname = "{}.mp4"
outputPath = os.path.join(cutsDir, fname)
# print(outputPath)

# Video Clip
clip = VideoFileClip(sourcePath)
# print(clip)

# clip attr
# fps = clip.reader.fps
# durationSec = clip.reader.duration
# nFrames = clip.reader.nframes
# fname = "{}.mp4"

def cutterFunc(sec,clip,outputDir):
    durationSec = clip.reader.duration
    n = ceil(durationSec / sec)
    tempStart = 0
    # print(n)
    for i in range(n):
        outputPath = os.path.join(outputDir, fname.format(i))
        if tempStart + sec > durationSec:
            subClip = clip.subclip(tempStart, durationSec)
            subClip.write_videofile(outputPath)
        else:    
            subClip = clip.subclip(tempStart, tempStart + sec)
            subClip.write_videofile(outputPath)
        tempStart += sec
cutterFunc(10, clip, cutsDir)
# print(ceil(100/25))
# print(ceil(durationSec-30))