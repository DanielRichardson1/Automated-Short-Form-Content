import praw
import os
from dotenv import load_dotenv


load_dotenv()
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')

# TODO: Hide credentials
reddit = praw.Reddit(
    user_agent=True,
    client_id="f0mPgBhUmOjUOoRNfS7JzA",
    client_secret="_59MAwRHzB12eot0iSTahyUx4HjYrA",
    username="Ok_Counter_4378",
    password="whatthesigma123"
)


def getPostAndComments(postUrl):
    post = reddit.submission(url=postUrl)

    print(post.title)
    print()
    print(post.selftext)

    for comment in post.comments:
        print()
        print(comment.body)


def getTopPostsToday(subreddit, postCount):
    subreddit = reddit.subreddit(subreddit)

    postsToday = []

    topPosts = subreddit.top(time_filter="day", limit=postCount)

    for post in topPosts:
        postsToday.append((post.title, post.selftext, post.url))

    return postsToday
