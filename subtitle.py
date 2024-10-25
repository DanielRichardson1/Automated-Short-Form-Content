import whisper
import cv2


def addSubtitles(audioFile, inVidPath, outVidPath, title_audio_duration):
    
    #
    # Get transcript from whisper
    #

    model = whisper.load_model('base')

    transcription = model.transcribe(
        audio=audioFile,
        word_timestamps=True,
        fp16=False
    )

    segments = transcription["segments"]

    words = {}

    for segment in segments:
        for word in segment["words"]:
            words[word["start"]] = word["word"]

    #
    # Load video
    #

    video = cv2.VideoCapture(inVidPath)

    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter(outVidPath, fourcc, fps, (width, height))


    time = 0
    # Read until video is completed
    while video.isOpened():
        # find the word to use
        ret, frame = video.read()
        if not ret:
            break

        word_to_use = ""
        for start_time, word in words.items():
            # TODO: add duration limiter
            if start_time <= title_audio_duration:
                word_to_use = ""
            elif start_time <= time:
                word_to_use = word
            else:
                break
        # increment time
        time += 1/fps
        # write the text
        writeText(word_to_use, frame, out)


    # Release everything if job is finished
    video.release()
    out.release()
    cv2.destroyAllWindows()


def writeText(text, frame, video_writer):
    # Add text to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    thickness = 10
    color = (255, 255, 255)
    border_color = (0, 0, 0)
    border_thickness = 5

    # Get text size
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_width, text_height = text_size

    # Calculate the center position
    pos_x = (frame.shape[1] - text_width) // 2
    pos_y = (frame.shape[0] - text_height) // 2
    position = (pos_x, pos_y)

    # Add the text to the frame
    cv2.putText(frame, text, position, font, font_scale,
                border_color, thickness + border_thickness * 2, cv2.LINE_AA)
    cv2.putText(frame, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

    # Write the frame with text
    video_writer.write(frame)
