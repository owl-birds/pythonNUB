from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.audio.fx.all import volumex
import os

# SOURCE PATH
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")
sourceAudioPath = os.path.join(SAMPLE_INPUTS, "audio.mp3")

# MAKING DIRECTORY
overlayDir = os.path.join(SAMPLE_OUTPUTS, "overlay")
os.makedirs(overlayDir, exist_ok=True)

# output path
oriAudioPath = os.path.join(overlayDir, "ori.mp3")
bgLowVolPath = os.path.join(overlayDir, "lowVolBg.mp3")
finalAudioPath = os.path.join(overlayDir, "overlayFinalAudio.mp3")
finalVideoPath = os.path.join(overlayDir, "overlayFinalVid.mp4")
introVideoPath = os.path.join(overlayDir, "intro.mp4")

# Video clip
clip = VideoFileClip(sourcePath)

originalAudio = clip.audio
# saving original audio from video file
#originalAudio.write_audiofile(oriAudioPath)

'''
mixing two different audio clip into one, and then bring it back
to the original audio
'''
# new audio
backgroundAudioClip = AudioFileClip(sourceAudioPath)
# making the bg music into the same length with the vid clip
# bg_music = backgroundAudioClip.subclip(0, clip.reader.duration)

introDuration = 5
fps = clip.reader.fps
w,h = clip.reader.size

introText = TextClip("HELLO WORLD!", fontsize=70, color="white", size=clip.size)
introText = introText.set_duration(introDuration)  # second
introText = introText.set_fps(fps)
introText = introText.set_pos("center")

# setting up an intro music
introMusic = backgroundAudioClip.subclip(0, introDuration)
introText = introText.set_audio(introMusic)

# watermark 
watermarkText = TextClip("WATERMARK BOOMER", fontsize=60, color="white", align="East", size=(w, 60))
# EAST : RIGHT SIDE
watermarkText = watermarkText.set_fps(fps)
watermarkText = watermarkText.set_duration(clip.reader.duration)
watermarkText = watermarkText.margin(left=2, right=2, bottom=2)
watermarkText = watermarkText.set_pos("bottom")

introText.write_videofile(introVideoPath)
# COMBINE
finalClip = CompositeVideoClip([clip, watermarkText], size=clip.size)
finalClip = finalClip.set_duration(clip.reader.duration)
finalClip = finalClip.set_fps(fps)
finalClip = concatenate_videoclips([introText, finalClip])
finalClip.write_videofile(finalVideoPath,codec="libx264",audio_codec="aac")
