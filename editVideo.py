from moviepy.editor import ImageSequenceClip, AudioFileClip, VideoFileClip
from random import randint


def combineAudioAndVideo(audioFile, videoFile, outputFile):
    # get audio length
    audio = AudioFileClip(audioFile)
    duration = audio.duration
    # get video for audio length
    video = VideoFileClip(videoFile)
    start = randint(0, 50*60)
    clip = video.subclip(start, start+duration)
    # combine video and audio
    clip.audio = audio
    clip.write_videofile(f"./output/{outputFile}.mp4")


def getAudioBack(audioFile, videoFile, outputFile):
    audio = AudioFileClip(audioFile)
    video = VideoFileClip(videoFile)
    video.audio = audio
    video.write_videofile(outputFile)

