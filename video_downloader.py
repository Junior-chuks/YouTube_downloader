from pytube import YouTube
import pytube
import shutil
import os
import pathlib
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Systems")
customtkinter.set_default_color_theme("blue")

the_link = None
interface = None

def video_downloader():
    """Downloads the video from YouTube via input link"""
    
    try:
        video_link = the_link.get()
        video = YouTube(video_link)
        stream = video.streams.get_highest_resolution()
        stream.download()
        video_relocator()
        interface.configure(text="Download complete !")

    except pytube.exceptions.VideoPrivate:
        print("It's private video")
    except Exception:
        interface.configure(text ="Download error")


def gui_interface():
    """creates the user interface that will take in links and execute the necessary funtions"""

    global the_link , interface
    # app frame
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("YouTube Downloader")
    
    #adding UI elements
    title = customtkinter.CTkLabel(app, text= "Insert a YouTube link", text_color="blue")
    title.pack(padx= 10 ,pady =10)

    #link input
    url_var = tkinter.StringVar()
    link = customtkinter.CTkEntry(app, width=350, height= 40 ,textvariable= url_var,text_color="red")
    link.pack()
    the_link = link
    #download button
    download = customtkinter.CTkButton(app, text= "Download" , text_color= "red",command=video_downloader)
    download.pack(padx=10,pady= 40)
    finished = customtkinter.CTkLabel(app,text="")
    finished.pack()
    interface = finished
    return app


def video_relocator():
    """relocates the video from the current folder to the videos folder"""
    for subdir ,dir ,files in os.walk("./"):
        for file in files:
            if ".mp4" in file:
                vid_name = file

    new_path = pathlib.Path.home()/"Videos"
    if vid_name:
        shutil.move(f"./{vid_name}",new_path)


if __name__ == "__main__":
    gui_interface().mainloop()

    