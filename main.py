import praw
import time
import json

with open("keys.json") as k:
    keysread = k.read()
keys = json.loads(keysread)
reddit = praw.Reddit(client_id=keys["client_id"],
                     client_secret=keys["client_secret"],
                     user_agent=keys["user_agent"],password=keys["password"],username=keys["username"])

for submission in reddit.subreddit("mindiapress").new():
    print(submission.title,submission.score,submission.url)
#    if "anti-national" in submission.selftext:
#        submission.reply("you said the A-word! :(")
#        time.sleep(3)
