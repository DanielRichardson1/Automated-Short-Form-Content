from reddit import getTopPostsToday
from narration import getNarration
from editVideo import combineAudioAndVideo, getAudioBack
from text import cropVideo
from subtitle import addSubtitles
from addImage import writeImage
from screenShot import getTitleScreenShot


if __name__ == "__main__":
    # Top 3 Posts from SubReddit
    posts = getTopPostsToday("hypotheticalsituation", 3)
    for i in range(0, len(posts)):
        print(f"Processing post {(i + 1)} of {len(posts)}...")
        post = posts[i]

        text_script = (post[0], post[1])

        print("Getting screenshot...")
        getTitleScreenShot(post[2], f"./screenShots/final{i}.png")

        print("Getting narration...")
        title_audo_duration = getNarration(text_script, f"audio{i}")  # TODO: Make voice less boring, probably more high-pitched
        
        print("Combining audio and video...")
        combineAudioAndVideo(f"./output/audio{i}.mp3", f"./videos/minecraft_parkour_1hr.mp4", f"pre-sub{i}")
        
        print("Cropping video...")
        cropVideo(f"./output/pre-sub{i}.mp4", f"./output/pre-sub-cropped{i}.mp4")
        
        print("Adding subtitles and adding audio back...")
        addSubtitles(f'./output/audio{i}.mp3', f'./output/pre-sub-cropped{i}.mp4', f'./output/post-sub-cropped{i}.mp4', title_audo_duration)

        print("Adding image to video...")
        writeImage(f'./output/post-sub-cropped{i}.mp4', f"./screenShots/final{i}.png", title_audo_duration, f'./output/post-image{i}.mp4')
        
        print("Getting audio back...")
        getAudioBack(f'./output/audio{i}.mp3', f'./output/post-image{i}.mp4', f'./FinishedContent/final_{i}.mp4')

    print("--------------------------------------")
    print("Finished, Content is ready!")
    print("--------------------------------------")







