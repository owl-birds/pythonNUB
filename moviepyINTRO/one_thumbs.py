from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os
from PIL import Image
# print(SAMPLE_INPUTS)
# print(SAMPLE_OUTPUTS)
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnailDir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnailFramesDir = os.path.join(SAMPLE_OUTPUTS,"frameThumbs")
# making a new directory based on the path you provide
os.makedirs(thumbnailDir, exist_ok=True)
os.makedirs(thumbnailFramesDir, exist_ok=True)
# print(sourcePath)

# initialize a clip file
clip = VideoFileClip(sourcePath)
#print(clip.reader.fps)  # FRAME PER SECOND
#print(clip.reader.nframes)
#print(clip.duration)  # SECONDS
duration = clip.reader.duration
max_duration = int(duration) + 1

# BASE ON SECONDS 
for i in range(0, max_duration):
    print("frame at {} seconds".format(i))
    frame = clip.get_frame(i)  # have to be integer
    #print(frame)  # numpy arrays : giving us a color
    # value for each individual pixels
    # can be useful for machine learning 
    # so the algorithm will learn from the color values
    #  in every frames
    newImgFilePath = os.path.join(thumbnailDir,"{}.jpg".format(i))
    newImg = Image.fromarray(frame)
    newImg.save(newImgFilePath)
# BASE ON FRAMES

# manual way finding seconds
fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes/ (fps*1.0) # to make sure python to round the nums

# PER FRAMES
# for i, frame in enumerate(clip.iter_frames()):
#     newImgFilePath = os.path.join(thumbnailFramesDir, f"{i}.jpg")
#     print(f"frame at {i} seconds saved at {newImgFilePath}")
#     newImg = Image.fromarray(frame)
#     newImg.save(newImgFilePath)

# FRAMES IN SECONDS, but saved on miliseconds (1 sec = 1000ms)
for i, frame in enumerate(clip.iter_frames()):
    if i % fps == 0:
        current_ms = (i/fps)*1000
        newImgFilePath = os.path.join(thumbnailFramesDir, f"{current_ms}.jpg")
        print(f"frame at {i} miliseconds saved at {newImgFilePath}")
        newImg = Image.fromarray(frame)
        newImg.save(newImgFilePath)

# USING ITER_FRAMES WILL BE MUCH FASTER THAN JUST USIG DURATION
