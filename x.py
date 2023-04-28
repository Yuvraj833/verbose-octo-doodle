import pytchat

import pytube

import subprocess

import time

# YouTube video link for pre-recorded video

video_link = "https://youtu.be/JNQ2chE_JJ0"

# YouTube Live Stream details

stream_key = "mdbd-ezyh-bekb-15hu-7myt"

stream_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

stream_cmd = f"ffmpeg -re -i \"{video_link}\" -c copy -f flv \"{stream_url}\""

# Start downloading pre-recorded video

video = pytube.YouTube(video_link)

video_stream = video.streams.get_highest_resolution()

video_stream.download()

# Start streaming pre-recorded video to YouTube Live

stream = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE)

time.sleep(10) # Wait for the stream to start before retrieving the Live Chat ID

# Retrieve Live Chat ID and start monitoring the chat

chat = pytchat.create(video_id=stream_key)

chat_id = chat.get_live_chat_id()

while chat.is_alive():

    for item in chat.get().sync_items():

        print(f"{item.datetime} [{item.author.name}]- {item.message}")

        # Process chat messages as needed

    time.sleep(1) # Add a small delay to avoid hitting the API too frequently
