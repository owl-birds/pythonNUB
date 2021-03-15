from conf import SAMPLE_OUTPUTS, SAMPLE_INPUTS
from moviepy.editor import *
import os
from PIL import Image

# VIDEO SOURCE
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")

# Making directory
cutDir = os.path.join(SAMPLE_OUTPUTS, "cutingVideo")
os.makedirs(cutDir, exist_ok=True)

# OUTPUT PATH
outputPath1 = os.path.join(cutDir, "cutVideo1.mp4")

clip = VideoFileClip(sourcePath)
subClip1 = clip.subclip(10, 15)
subClip1.write_videofile(outputPath1)
clip.close()
subClip1.close()