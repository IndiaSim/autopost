import praw
import time
import json

with open("keys.json") as k:
    keysread = k.read()
keys = json.loads(keysread)
reddit = praw.Reddit(client_id=keys["client_id"],
                     client_secret=keys["client_secret"],
                     user_agent=keys["user_agent"],password=keys["password"],username=keys["username"])

subreddit = reddit.subreddit("mindia")
