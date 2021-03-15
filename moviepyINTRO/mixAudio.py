from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.audio.fx.all import volumex
import os

# SOURCE PATH
sourcePath = os.path.join(SAMPLE_INPUTS, "sample.mp4")
sourceAudioPath = os.path.join(SAMPLE_INPUTS, "audio.mp3")

# MAKING DIRECTORY
mixAudioDir = os.path.join(SAMPLE_OUTPUTS, "mixedAudio")
os.makedirs(mixAudioDir, exist_ok=True)

# output path
oriAudioPath = os.path.join(mixAudioDir, "ori.mp3")
bgLowVolPath = os.path.join(mixAudioDir, "lowVolBg.mp3")
finalAudioPath = os.path.join(mixAudioDir, "finalAudio.mp3")
finalVideoPath = os.path.join(mixAudioDir, "finalVid.mp4")

# Video clip
clip = VideoFileClip(sourcePath)

originalAudio = clip.audio
# saving original audio from video file
originalAudio.write_audiofile(oriAudioPath)

'''
mixing two different audio clip into one, and then bring it back
to the original audio
'''
# new audio
backgroundAudioClip = AudioFileClip(sourceAudioPath)
# making the bg music into the same length with the vid clip
bg_music = backgroundAudioClip.subclip(0, clip.reader.duration)
#changing volume
#bg_music = bg_music.volume(0.10)  # 10% of the original volume
bg_music = bg_music.fx(volumex,0.10)
bg_music.write_audiofile(bgLowVolPath)

# COMBINE TWO AUDIO CLIPS
# COMPOSITE LAYER ON TOP OF ONE ANOTHERS
# CONCATNATE COMBINE TWO AUDIO
finalAudio = CompositeAudioClip([originalAudio, bg_music])
finalAudio.write_audiofile(finalAudioPath, fps=originalAudio.fps)
# final audio dont have fps


# COMBINE THE CLIP WITH THE AUDIO
finalClip = clip.set_audio(finalAudio)
# if the audio dont play in final vid
finalClip.write_videofile(finalVideoPath, codec="libx264", audio_codec = "aac")
# original
# finalClip.write_videofile(finalVideoPath)