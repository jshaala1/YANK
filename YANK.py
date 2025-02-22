import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import argparse
import re
import csv

def is_valid_youtube_url(url):
    """Validates if the given URL is a valid YouTube URL.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is a valid YouTube URL, False otherwise.
    """
    youtube_regex = (
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|playlist\?list=|(?:v|e(?:mbed)?)\S*?[?&]v=)[a-zA-Z0-9_-]+'
    )
    return re.match(youtube_regex, url) is not None


def download_video(video_url, save_path=".", format_choice="webm"):
    """Downloads a YouTube video using yt-dlp and saves it in the specified format and location.

    Args:
        video_url (str): The URL of the video to download.
        save_path (str): The directory to save the downloaded video. Defaults to current directory.
        format_choice (str): The desired video format (e.g., "mp4", "mkv", "webm"). Defaults to "webm".
    """
    if not is_valid_youtube_url(video_url):
        messagebox.showerror("Error", f"Invalid YouTube URL: {video_url}")
        return

    try:
        ydl_opts = {
            'format': f'bestvideo[ext={format_choice}]+bestaudio[ext={format_choice}]/best[ext={format_choice}]',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': format_choice,
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            messagebox.showinfo("Success", f"Downloaded: {info_dict['title']}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def process_input(video_urls, save_path, format_choice, audio_only, subtitles, download_thumbnail):
    for link in video_urls:
        download_video(link, save_path, format_choice, audio_only, subtitles, download_thumbnail)


def browse_file():
    """Opens a file dialog to select a CSV file containing YouTube URLs."""
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    url_entry.delete(0, tk.END)
    url_entry.insert(0, filename)


def browse_directory():
    """Opens a directory dialog to select the save location for the downloaded videos."""
    directory = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(0, directory)


def read_csv(file_path):
    """Reads YouTube URLs from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing YouTube URLs.

    Returns:
        list: A list of YouTube URLs from the CSV file.
    """
    urls = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Assuming URLs are in the first column of the CSV file
                if row:
                    urls.append(row[0].strip())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read CSV file: {str(e)}")
    return urls


def run_gui():
    # GUI setup
    root = tk.Tk()
    root.title("YouTube Video Downloader")

    tk.Label(root, text="Enter YouTube URL or select a text file:").pack()
    global url_entry
    url_entry = tk.Entry(root, width=50)
    url_entry.pack()
    tk.Button(root, text="Browse", command=browse_file).pack()

    tk.Label(root, text="Select save location:").pack()
    global save_path_entry
    save_path_entry = tk.Entry(root, width=50)
    save_path_entry.pack()
    tk.Button(root, text="Browse", command=browse_directory).pack()

    tk.Label(root, text="Select video format:").pack()
    format_var = tk.StringVar(value="webm")
    tk.OptionMenu(root, format_var, "mp4", "mkv", "webm").pack()

    # Checkbox for audio-only download
    audio_only_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Audio only", variable=audio_only_var).pack()

    # Checkbox for subtitles download
    subtitles_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download subtitles", variable=subtitles_var).pack()

    # Checkbox for downloading thumbnail
    thumbnail_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download thumbnail", variable=thumbnail_var).pack()

    def on_download():
        input_source = url_entry.get()
        save_path = save_path_entry.get() or "."
        format_choice = format_var.get()
        audio_only = audio_only_var.get()
        subtitles = subtitles_var.get()
        download_thumbnail = thumbnail_var.get()  # Get the value of the thumbnail checkbox
        
        if os.path.isfile(input_source):
            with open(input_source, "r") as file:
                links = [line.strip() for line in file.readlines() if line.strip()]
        else:
            links = [input_source]
        
        process_input(links, save_path, format_choice, audio_only, subtitles, download_thumbnail)
    
    tk.Button(root, text="Download", command=on_download).pack()
    root.mainloop()


def run_cli(args):
    input_source = args.input
    save_path = args.save_path
    format_choice = args.format
    audio_only = args.audio_only
    subtitles = args.subtitles
    download_thumbnail = args.thumbnail
    
    if os.path.isfile(input_source):
        with open(input_source, "r") as file:
            links = [line.strip() for line in file.readlines() if line.strip()]
    else:
        links = [input_source]
    
    process_input(links, save_path, format_choice, audio_only, subtitles, download_thumbnail)

def main():
    if len(sys.argv) > 1:
        # Run as a CLI tool
        parser = argparse.ArgumentParser(
            description="A simple tool to download YouTube videos via URL or a text file with URLs. Optionally choose a save location, video format, audio, subtitles, or thumbnail."
        )
        parser.add_argument('input', help="YouTube URL or path to a text file with URLs")
        parser.add_argument('--save_path', default=".", help="Directory to save the downloaded videos (default: current directory)")
        parser.add_argument('--format', choices=['mp4', 'mkv', 'webm'], default='webm', help="Video format (default: webm)")
        parser.add_argument('--audio_only', action='store_true', help="Download audio only")
        parser.add_argument('--subtitles', action='store_true', help="Download subtitles")
        parser.add_argument('--thumbnail', action='store_true', help="Download thumbnail")
        
        args = parser.parse_args()
        run_cli(args)
    else:
        # Run as a GUI tool
        run_gui()


if __name__ == "__main__":
    main()
