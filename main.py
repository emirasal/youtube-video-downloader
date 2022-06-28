import tkinter as tk

from pathlib import Path
from video_D import video_download

def on_click():
    url = textbox.get()
    res = on_start.get()

    downloads_path = str(Path.home() / "Downloads")[2:]
    try:
        video_download(downloads_path, url, res)
        done = tk.Label(root, text="Finished Downloading", font=("Orator Std", 12), width=30)
        done.config(fg="green")
        done.pack()
        done.after(9000, done.destroy)
    except:
        error = tk.Label(root, text="Invalid YouTube Link, try another.", font=("Orator Std", 12), width=30)
        error.config(fg="red")
        error.pack()
        error.after(7000, error.destroy)

root = tk.Tk()
root.geometry("750x300")
root.title("YouTube Video Downloader")

label = tk.Label(root, text="Welcome to YouTube Video Downloader, enter your link below:", font=("Orator Std", 12), width=75)
label.pack(padx=10, pady=10)

# Url Entry
textbox = tk.Entry(root, font=("Arial", 12), width=76)
textbox.pack(pady = 15)
textbox.insert(0, "Enter your youtube link here")


l = tk.Label(root, text="You can change the video Quality:", font=("Orator Std", 12), width=70)
l.pack()

# Resolution Entry
resolution_list = [
    "Highest Resolution", 
    "1080p",
    "720p",
    "480p",
    "360p",
    ]

on_start = tk.StringVar()
on_start.set(resolution_list[0])

resolution_box = tk.OptionMenu(root, on_start, *resolution_list)
resolution_box.pack()

# Submit Button 
Button = tk.Button(root, text= "Start Downloading", command=on_click, width=35, bg="#20bebe", fg="white", height=2)
Button.pack(padx = 6, pady = 10)


desc1 = tk.Label(root, text="Video will be downloaded to your computer's 'Downloads Folder'.", font=("Orator Std", 11), width=70)
desc1.pack()
desc2 = tk.Label(root, text="Program may freeze couple of seconds after clicking 'Start Downloading' that means downloading process have started.", font=("Orator Std", 10), width=90)
desc2.place(relx = 0.0, rely = 1.0, anchor="sw")

root.mainloop()