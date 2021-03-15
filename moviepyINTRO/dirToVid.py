from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * # ImageClip
import os
from PIL import Image
# print(SAMPLE_INPUTS)
# print(SAMPLE_OUTPUTS)
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnailDir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnailFramesDir = os.path.join(SAMPLE_OUTPUTS, "frameThumbs")
outputVideo = os.path.join(SAMPLE_OUTPUTS, "thumbs.mp4")
outputVideo2 = os.path.join(SAMPLE_OUTPUTS, "thumbs2.mp4")
outputVideo3 = os.path.join(SAMPLE_OUTPUTS, "thumbs3.mp4")

thisDir = os.listdir(thumbnailDir)
filePaths = [os.path.join(thumbnailDir,fname) for fname in thisDir if fname.endswith("jpg")]
#print(filePaths)
#filepath is out of order
# clip = ImageSequenceClip(filePaths, fps=10)
# clip.write_videofile(outputVideo)

'''
to make the the file to be in order
'''
filePaths2 = []
directory = {}
for folder, subfolders, files in os.walk(thumbnailDir):
    # filePaths2 = [fname for fname in files if fname.endswith("jpg")]
    for fname in files:
        filepath = os.path.join(folder, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath
        #print(filepath)
for key in sorted(directory.keys()):
    filePaths2.append(directory[key])
#print(filePaths2)
# MAKING THE VIDEO
# clip = ImageSequenceClip(filePaths2, fps=10)
# clip.write_videofile(outputVideo2)

# TRUNING EACH INDIVIDUAL FILE PATH into FRAME ITSELF
myClips = []
for path in list(filePaths2):
    frame = ImageClip(path)
    myClips.append(frame.img)
    # print(dir(frame))
    # frame.img : numppy array full of color values per pixels
clip = ImageSequenceClip(myClips, fps=10)
clip.write_videofile(outputVideo3)