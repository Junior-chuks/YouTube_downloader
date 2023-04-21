# YouTube Video Downloader

This is a Python script that downloads a YouTube video given a video link. It utilizes the pytube library to download the
 video and the customtkinter library to create the user interface.
 ![Screenshot from 2023-04-21 21-59-19](https://user-images.githubusercontent.com/128588228/233744497-05bba0da-e4e6-4279-bb17-5aafc3990df6.png)
![Screenshot from 2023-04-21 22-02-26](https://user-images.githubusercontent.com/128588228/233744739-f2a883c0-661f-4e4e-ae7f-11d7f78f57bb.png)

![Screenshot from 2023-04-21 22-00-35](https://user-images.githubusercontent.com/128588228/233744722-83797e49-005e-4c54-b8cc-254ed2cbf31b.png)

![Screenshot from 2023-04-22 00-46-18](https://user-images.githubusercontent.com/128588228/233745449-4a9b37c4-7c93-4e89-8f63-f5bf1f34d580.png)

![Screenshot from 2023-04-22 00-46-36](https://user-images.githubusercontent.com/128588228/233745462-b3e7c6e8-6cef-4f1a-97b9-f03190fc9373.png)

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
python3 video_downloader.py
```

2. A GUI window will appear where you can input the YouTube link and click the "Download" button.

3. Once the download is complete, the script will move the video to the user's "Videos" folder.

## Notes

- The downloaded video will be saved in the highest available resolution.
- If the video is private, the script will not download it.
- If there is an error during the download, the GUI will display an error message.
- The script will only download one video at a time.
