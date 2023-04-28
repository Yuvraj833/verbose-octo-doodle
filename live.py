import pafy

import cv2

import pyautogui

import numpy as np

import time

# YouTube video link for live streaming

video_link = "https://youtu.be/7ssp44DydyA"

# YouTube Live Stream details

stream_key = "mdbd-ezyh-bekb-15hu-7myt"

# Load video using pafy

video = pafy.new(video_link)

# Get best video stream

best_video_stream = video.getbest()

# Start capturing frames from the video

cap = cv2.VideoCapture(best_video_stream.url)

# Define the codec and create a VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Wait for 5 seconds to make sure the video is playing

time.sleep(5)

# Start the live stream

while True:

    ret, frame = cap.read()

    if not ret:

        break

    # Resize the frame to 640x480

    resized_frame = cv2.resize(frame, (640, 480))

    # Write the resized frame to the output file

    out.write(resized_frame)

    # Display the frame in a window (optional)

    cv2.imshow('frame', resized_frame)

    # Send the frame to YouTube Live using PyAutoGUI

    pyautogui.hotkey('ctrl', 'shift', 'alt', 'p')

    pyautogui.typewrite(stream_key)

    pyautogui.press('enter')

    pyautogui.screenshot('dummy.png') # This line is needed to prevent PyAutoGUI from getting stuck

    time.sleep(1) # Add a small delay to avoid hitting the API too frequently

    # Exit the loop if 'q' is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

# Release everything

cap.release()

out.release()

cv2.destroyAllWindows()

