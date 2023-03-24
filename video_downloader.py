from pytube import YouTube
import pytube
import shutil
import os
import pathlib


def video_downloader():
    """Downloads the video from YouTube via input link"""
    
    try:
        video_link = str(input("Please enter video url :"))
        video = YouTube(video_link)
        stream = video.streams.get_highest_resolution()
        loader_animation()
        stream.download()
        video_relocator()

    except pytube.exceptions.VideoPrivate:
        print("It's private video")


def loader_animation():
    """
    Creates a loading animation that's displayed on the user interface
    Param: 
    """
    import time
    import sys
    print("⚪ Downloading video")

    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□ 10%]","[■■□□□□□□□□ 20%]", "[■■■□□□□□□□ 30%]", "[■■■■□□□□□□ 40%]",
                "[■■■■■□□□□□ 50%]", "[■■■■■■□□□□ 60%]", "[■■■■■■■□□□ 70%]", "[■■■■■■■■□□ 80%]",
                "[■■■■■■■■■□ 90%]", "[■■■■■■■■■■ 100%]"]

    for i in range(len(animation)):
        time.sleep(0.5)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n🟢 Download complete")


def video_relocator():
    for subdir ,dir ,files in os.walk("./"):
        for file in files:
            if ".mp4" in file:
                vid_name = file

    new_path = pathlib.Path.home()/"Videos"
    if vid_name:
        shutil.move(f"./{vid_name}",new_path)

if __name__ == "__main__":
    video_downloader()
    # 'dir = pathlib.Path("~/downloads/")
    
    


