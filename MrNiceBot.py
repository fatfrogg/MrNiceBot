import praw
import re
import os
import random

niceQuotes = \
    [
        "Hey, just wanted to let you know that are a wonderful and unique individual!",
        "You are amazing, keep up the good work!",
        "Are you having a good day? Try to think of something you are thankful for, and express that gratitude!",
        "Have you helped anybody out today?",
        "I am a robot, but I still think you are pretty cool :)",
        "You are a gift to the people in your life!",
        "Cherish every moment, don't lose sight of what makes you happy!",
        "Thanks for being you :)",
        "You are truly one of a kind",
        "You are strong, and have a great heart. Keep it up!",
        "Never compromise on being yourself",
        "Your potential is limitless!",
        "It's the small things that count",
        "You a ray of sunshine in the darkness :)",
    ]

reddit = praw.Reddit('bot1')

#.txt file to store posts already replied to
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n") #split to create list of ids
        posts_replied_to = list(filter(None, posts_replied_to))#get rid of empty values


#Create subreddit instance
subreddit = reddit.subreddit("all")

#Get the top 5 hot submissions
for submission in subreddit.hot(limit=10):
    if(submission.id not in posts_replied_to):#If bot has not yet replied to this post
        replyQuote = random.choice(niceQuotes)
        submission.reply(replyQuote)#Reply to the post
        print("Bot replied to : ", submission.title)
        posts_replied_to.append(submission.id)#add to list of replied posts
        
            

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


