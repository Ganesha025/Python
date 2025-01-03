import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from yt_dlp import YoutubeDL

def select_download_path():
    """Open a dialog to select the download folder."""
    folder = filedialog.askdirectory()
    download_path.set(folder)

def download_video():
    """Download the YouTube video using yt-dlp."""
    url = video_url.get()
    path = download_path.get()

    if not url.strip():
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    if not path.strip():
        messagebox.showerror("Error", "Please select a download path.")
        return

    try:
        # yt-dlp options
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'best',  # Download the best quality video
        }

        status_label.config(text="Downloading...", fg="blue")
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.config(text="Download complete!", fg="green")
        messagebox.showinfo("Success", f"Video downloaded successfully!\nSaved to: {path}")
    except Exception as e:
        status_label.config(text="Download failed.", fg="red")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
app = Tk()
app.title("YouTube Video Downloader")
app.geometry("500x300")
app.resizable(False, False)

# Variables for storing input
video_url = StringVar()
download_path = StringVar()

# UI Elements
Label(app, text="YouTube Video Downloader", font=("Arial", 16, "bold")).pack(pady=10)

Label(app, text="Enter YouTube URL:", font=("Arial", 12)).pack(pady=5)
Entry(app, textvariable=video_url, width=50).pack(pady=5)

Label(app, text="Select Download Path:", font=("Arial", 12)).pack(pady=5)
Entry(app, textvariable=download_path, width=50, state="readonly").pack(pady=5)
Button(app, text="Browse", command=select_download_path).pack(pady=5)

Button(app, text="Download Video", command=download_video, bg="blue", fg="white", font=("Arial", 12)).pack(pady=20)

status_label = Label(app, text="", font=("Arial", 12))
status_label.pack(pady=10)

# Run the application
app.mainloop()
