import cv2
import numpy as np
import pyautogui
import time
import requests
import smtplib
from email.mime.text import MIMEText
import os
import configparser
from sys import platform

config = configparser.ConfigParser()
config.read(filenames="config.ini")

SLACK_WEBHOOK_URL = config["SLACK"]["webhook"]

# TODO attach the file in slack message


# Function to send Slack message
def send_slack_message(message, screenshot_path=""):
    payload = {"text": message}
    if platform == "darwin":
        os.system("afplay /System/Library/Sounds/Sosumi.aiff")
    if screenshot_path == "":
        requests.post(SLACK_WEBHOOK_URL, json=payload)


def capture_screen():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)


def monitor_screen(threshold=30, interval=int(config["SYS"]["INTERVAL"]), notify_via="slack"):
    time.sleep(interval)
    temp_screen = capture_screen()
    curr_screen = capture_screen()
    while True:
        curr_screen = capture_screen()
        diff = cv2.absdiff(temp_screen, curr_screen)
        non_zero_count = np.count_nonzero(diff)
        # print(" ----> ",non_zero_count)
        if non_zero_count > threshold:
            temp_screen = capture_screen()
            print("Screen content changed")
            message = "New Message!"
            if notify_via == "slack":
                send_slack_message(message)

        time.sleep(interval)


if __name__ == "__main__":
    # Start program  after n seconds
    time.sleep(int(config["SYS"]["INITIAL_SLEEP"]))
    print("Monitoring screen for changes...")
    monitor_screen(notify_via="slack")
