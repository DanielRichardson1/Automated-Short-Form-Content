# Daily Reddit Shortform Video Generator

This project scrapes the top 3 posts from a given subreddit daily and generates shortform content by adding narration, video, and subtitles. The final output is a video file, ready to be posted or shared. The project currently uses a Minecraft parkour video as background, generates a narration based on post content, and adds per-word subtitles for clarity.

## Features

- Automatically scrapes the top 3 posts from a specified subreddit.
- Generates an engaging shortform video with narration, subtitles, and background video.
- Processes text and media files to create the final product.
- Easy to customize the subreddit and the video background.

## How It Works

1. Scrape the top 3 posts from the subreddit.
2. Create a script from the post titles and text.
3. Generate narration from the script (text-to-speech).
4. Combine the narration with a video background.
5. Crop and add subtitles to the final video.
6. Output is a shareable shortform video.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- `pip` (Python package installer)
- A .env file with Reddit account and API credentials (for PRAW)

### Steps

1. **Clone the repository**  
   Clone this GitHub repository to your local machine
   ```bash
   git clone https://github.com/your-username/reddit-shortform-generator.git
   cd reddit-shortform-generator
   ```
2. **Add your .env file**  
   Once you have the keys, create a .env file in the project root directory and add the following
   ```bash
   CLIENT_ID=your_reddit_client_id
   CLIENT_SECRET=your_reddit_client_secret
   USER_AGENT=your_reddit_user_agent
   ```
3. **Run the script**  
   You can run the script to generate content with the top 3 posts from the last 24 hours
   ```bash
   python main.py
   ```

Test
