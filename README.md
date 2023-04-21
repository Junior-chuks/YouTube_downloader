# YouTube Video Downloader

This is a Python script that downloads a YouTube video given a video link. It utilizes the pytube library to download the video and the customtkinter library to create the user interface.

## Prerequisites

- Python 3
- pytube library
- customtkinter library
- tkinter library

## Installation

You can install the necessary libraries via pip:

```
pip install pytube customtkinter tk
```

## Usage

1. Run the script via the command line:
```
python video_downloader.py
```

2. A GUI window will appear where you can input the YouTube link and click the "Download" button.

3. Once the download is complete, the script will move the video to the user's "Videos" folder.

## Notes

- The downloaded video will be saved in the highest available resolution.
- If the video is private, the script will not download it.
- If there is an error during the download, the GUI will display an error message.
- The script will only download one video at a time.