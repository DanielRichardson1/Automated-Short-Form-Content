from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip


def writeImage(video_path, image_path, image_duration, output_path):
    # Load your video
    video = VideoFileClip(video_path)

    # Load your image and set its duration and position
    image = ImageClip(image_path).set_duration(image_duration)  # Duration in seconds

    # Resize the image if needed and set its position (center by default)
    image = image.resize(height=75).set_position(("center", "center"))

    # Set the starting time for the image to appear over the video
    image = image.set_start(0)  # Start at 0 seconds into the video

    # Combine the video and image
    final = CompositeVideoClip([video, image])

    # Save the result
    final.write_videofile(output_path, codec="libx264")
