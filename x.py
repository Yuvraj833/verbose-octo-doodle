import subprocess

import pafy

from pydub import AudioSegment

import requests

# Replace with the URL of your pre-recorded video file

video_url = "https://youtu.be/B3nfjlD1zvk"

# Replace with your YouTube stream key

stream_key = "mdbd-ezyh-bekb-15hu-7myt"

# Download the video file using requests library

video_content = requests.get(video_url).content

# Load the video content using FFmpeg and resize to 480p resolution

video = (

    ffmpeg

    .input("pipe:0")

    .filter("scale", "480:-2")

    .output("pipe:", format="flv",
