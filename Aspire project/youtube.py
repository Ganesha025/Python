import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox, Frame
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
app.geometry("600x400")
app.resizable(False, False)
app.config(bg="#f5f5f5")  # Light grey background

# Variables for storing input
video_url = StringVar()
download_path = StringVar()

# UI Elements
header_frame = Frame(app, bg="#4a90e2", height=60)
header_frame.pack(fill="x")

Label(
    header_frame, 
    text="YouTube Video Downloader", 
    font=("Helvetica", 18, "bold"), 
    bg="#4a90e2", 
    fg="white"
).pack(pady=10)

content_frame = Frame(app, bg="#f5f5f5")
content_frame.pack(pady=20)

# URL Input
Label(
    content_frame, 
    text="Enter YouTube URL:", 
    font=("Arial", 12), 
    bg="#f5f5f5"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")
Entry(
    content_frame, 
    textvariable=video_url, 
    width=50, 
    font=("Arial", 12), 
    borderwidth=2, 
    relief="groove"
).grid(row=0, column=1, padx=10, pady=10)

# Download Path Selection
Label(
    content_frame, 
    text="Select Download Path:", 
    font=("Arial", 12), 
    bg="#f5f5f5"
).grid(row=1, column=0, padx=10, pady=10, sticky="w")
Entry(
    content_frame, 
    textvariable=download_path, 
    width=50, 
    font=("Arial", 12), 
    state="readonly", 
    borderwidth=2, 
    relief="groove"
).grid(row=1, column=1, padx=10, pady=10)
Button(
    content_frame, 
    text="Browse", 
    command=select_download_path, 
    font=("Arial", 10), 
    bg="#4caf50", 
    fg="white", 
    activebackground="#45a049", 
    relief="flat", 
    width=10
).grid(row=1, column=2, padx=10, pady=10)

# Download Button
Button(
    app, 
    text="Download Video", 
    command=download_video, 
    font=("Arial", 14, "bold"), 
    bg="#ff5722", 
    fg="white", 
    activebackground="#e64a19", 
    relief="flat", 
    width=20
).pack(pady=20)

# Status Label
status_label = Label(
    app, 
    text="", 
    font=("Arial", 12), 
    bg="#f5f5f5", 
    fg="black"
)
status_label.pack(pady=10)

# Run the application
app.mainloop()
