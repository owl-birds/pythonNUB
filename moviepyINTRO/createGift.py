from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os
from PIL import Image
from moviepy.video.fx.all import crop


# SOURCE PATH
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")

# making directory
gifDir = os.path.join(SAMPLE_OUTPUTS, "sampleGif")
os.makedirs(gifDir, exist_ok=True)
# OUPUT PATH
outputPath1 = os.path.join(gifDir, "sample1.gif")
outputPath2 = os.path.join(gifDir, "sample2.gif")
outputPath3 = os.path.join(gifDir, "croppedGif1.gif")

clip = VideoFileClip(sourcePath)
fps = clip.reader.fps
duration = clip.reader.duration
nFrames = clip.reader.nframes

subClip = clip.subclip(10, 20)
subClip = subClip.resize(width=320)
# subClip.write_gif(outputPath1)
# IT WILL BE USING FFMPPEG
# subClip.write_gif(outputPath2, fps=20, program="ffmpeg")

width, height = clip.size
subClip2 = clip.subclip(10, 20)
squaredCroppedClip = crop(subClip2, width=320, height=320, x_center=width / 2, y_center=height / 2)
squaredCroppedClip.write_gif(outputPath3, fps=fps, program="ffmpeg")
