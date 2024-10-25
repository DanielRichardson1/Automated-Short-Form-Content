import cv2


def cropVideo(inputPath, outputPath):

    # Load the input video
    video = cv2.VideoCapture(inputPath)

    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 9:16 aspect ratio (vertical video)
    target_aspect_ratio = 9 / 16

    # Check whether to crop vertically or horizontally
    if width / height > target_aspect_ratio:
        # Video is wider than 9:16, crop horizontally
        new_width = int(height * target_aspect_ratio)
        x_offset = (width - new_width) // 2
        y_offset = 0
        crop_width = new_width
        crop_height = height
    else:
        # Video is taller than 9:16, crop vertically
        new_height = int(width / target_aspect_ratio)
        y_offset = (height - new_height) // 2
        x_offset = 0
        crop_width = width
        crop_height = new_height

    # Define the codec and create a VideoWriter object to save the cropped video
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')  # Codec for MP4
    out = cv2.VideoWriter(outputPath, fourcc, fps, (crop_width, crop_height))

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Crop the frame (x_offset, y_offset, width, height)
        cropped_frame = frame[y_offset:y_offset + crop_height, x_offset:x_offset + crop_width]

        # Write the cropped frame to the output video
        out.write(cropped_frame)

    # Release everything
    video.release()
    out.release()
    cv2.destroyAllWindows()


def addSubtitles(inputPath, outputPath, script, audio):
    # Load video
    video = cv2.VideoCapture(inputPath)

    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter(outputPath, fourcc, fps, (width, height))

    while video.isOpened():
        for i in range(5*30):

            ret, frame = video.read()
            if not ret:
                break

            writeText("hello", frame, out)

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


# addSubtitles(inputPath="./output/pre-sub-cropped.mp4", outputPath="./output/post-sub.mp4")
