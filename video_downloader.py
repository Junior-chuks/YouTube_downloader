from pytube import YouTube
import pytube
import shutil
import os
import pathlib
import tkinter
import customtkinter
import threading

customtkinter.set_appearance_mode("Systems")
customtkinter.set_default_color_theme("blue")

the_link = None
interface = None
progress_bar = None
download_btn = None

def download_video_with_thread():
    global download_btn
    download_btn.configure(state = "disabled")
    downloader = threading.Thread(target = video_downloader)
    downloader.start()

def video_downloader():
    """Downloads the video from YouTube via input link"""
    
    global download_btn

    try:
        video_link = the_link.get()
        video = YouTube(video_link)
        video.register_on_progress_callback(on_download_progress)
        stream = video.streams.get_highest_resolution()
        stream.download()
        video_relocator()
        interface.configure(text="Download complete !")
    except pytube.exceptions.VideoPrivate:
        interface.configure(text = "It's private video")
    except Exception:
        interface.configure(text ="Download error")
    finally:
        download_btn.configure(state = "normal")

def gui_interface():
    """creates the user interface that will take in links and execute the necessary funtions"""

    global the_link , interface, progress_bar, download_btn
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
    download_btn = customtkinter.CTkButton(app, text= "Download" , text_color= "red",command = download_video_with_thread)
    download_btn.pack(padx=10,pady= 40)

    #progress bar
    progress_bar = customtkinter.CTkProgressBar(app, width = 350, height = 10, corner_radius = 5)
    progress_bar.pack()
    progress_bar.set(0)

    # Result label
    finished = customtkinter.CTkLabel(app,text="")
    finished.pack()
    interface = finished
    return app

def on_download_progress(stream, chunk, remaining_bytes):
    """Update the progress bar"""
    global progress_bar
    file_size = stream.filesize
    current_downloaded = file_size - remaining_bytes
    progress_bar.set(current_downloaded / file_size)

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