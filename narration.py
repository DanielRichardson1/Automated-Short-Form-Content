import playsound
from openai import OpenAI
import os
from moviepy.editor import AudioFileClip, concatenate_audioclips



def getNarration(script_tuple, fileName):
    
    title_script = script_tuple[0] + "                    "
    body_script = script_tuple[1] + "... What would you do?"

    client = OpenAI()
    with client.audio.speech.with_streaming_response.create(
        input=title_script,
        model="tts-1",
        voice="onyx",
    ) as response:
        response.stream_to_file(f"./output/{fileName}_title.mp3")
    
    with client.audio.speech.with_streaming_response.create(
        input=body_script,
        model="tts-1",
        voice="onyx",
    ) as response:
        response.stream_to_file(f"./output/{fileName}_body.mp3")
    
    title_audio = AudioFileClip(f"./output/{fileName}_title.mp3")
    title_audio_duration = title_audio.duration
    
    body_audio = AudioFileClip(f"./output/{fileName}_body.mp3")
    combined_audio = concatenate_audioclips([title_audio, body_audio])
    combined_audio.write_audiofile(f"./output/{fileName}.mp3")

    title_audio.close()
    body_audio.close()

    
    return title_audio_duration
