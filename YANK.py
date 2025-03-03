import os
import sys
import argparse
import re
import yt_dlp
import subprocess
import platform
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

DEFAULT_FORMAT = "webm"
DEFAULT_SAVE_PATH = "."


def get_ffmpeg_path():
    """Finds the ffmpeg binary based on the OS and PyInstaller bundle status."""
    is_windows = platform.system() == "Windows"
    ffmpeg_filename = "ffmpeg.exe" if is_windows else "ffmpeg"

    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, ffmpeg_filename)
    
    return ffmpeg_filename  # Default for regular Python execution (expects ffmpeg in PATH)

def is_ffmpeg_working(ffmpeg_path):
    """Checks if ffmpeg is available and working."""
    try:
        result = subprocess.run([ffmpeg_path, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

def check_ffmpeg():
    """Ensures ffmpeg is available, otherwise exits."""
    ffmpeg_path = get_ffmpeg_path()

    # Ensure ffmpeg is executable on Linux/macOS
    if platform.system() != "Windows" and os.path.exists(ffmpeg_path):
        os.chmod(ffmpeg_path, 0o755)

    if not is_ffmpeg_working(ffmpeg_path):
        sys.exit("Error: ffmpeg is required. Install it or include it in the exe.")

    print(f"Using ffmpeg at: {ffmpeg_path}")

check_ffmpeg()

def is_valid_youtube_url(url):
    """Validates if the given URL is a YouTube link."""
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+' 
    return re.match(youtube_regex, url) is not None

def progress_hook(d):
    """Updates the progress bar only if running in GUI mode."""
    if 'progress_bar' in globals():  # This means GUI mode is active
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', d.get('total_bytes_estimate', 1))
            percent = int((downloaded / total) * 100)

            try:
                progress_bar["value"] = percent
                progress_label.config(text=f"Downloading... {percent}%")
                root.update_idletasks()
            except Exception:
                pass

        elif d['status'] == 'finished':
            progress_label.config(text="Download complete!")

def download_video(video_url, save_path, format_choice, audio_only, subtitles, download_thumbnail):
    """Downloads the video with given options."""
    import tkinter.messagebox as messagebox  

    try:
        # Define format selection mapping
        format_map = {
            'webm': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best',
            'mp4': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'mkv': 'bestvideo+bestaudio/best'
        }
        
        # Ensure format choice is valid
        format_selection = format_map.get(format_choice, 'best')

        ydl_opts = {
            'ffmpeg_location': get_ffmpeg_path(),  
            'format': format_selection, 
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook]
        }

        if audio_only:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]
            })

        if subtitles:
            ydl_opts['writesubtitles'] = True
            ydl_opts['subtitleslangs'] = ['en']

        if download_thumbnail:
            ydl_opts['writethumbnail'] = True

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

            # Only show success message in GUI mode
            if 'progress_bar' in globals() and 'progress_label' in globals():
                messagebox.showinfo("Success", f"Downloaded: {info['title']}")

        if 'progress_bar' in globals() and 'progress_label' in globals():
            progress_bar["value"] = 0
            progress_label.config(text="Download complete!")

    except yt_dlp.utils.DownloadError as e:
        if 'progress_label' in globals():
            messagebox.showerror("Download Error", str(e))
    except Exception as e:
        if 'progress_label' in globals():
            messagebox.showerror("Error", str(e))


def process_input(video_urls, save_path, format_choice, audio_only, subtitles, download_thumbnail):
    """Processes URLs and starts download."""
    for link in video_urls:
        download_video(link, save_path, format_choice, audio_only, subtitles, download_thumbnail)

def browse_file():
    """Opens file dialog for text file."""
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    url_entry.delete(0, tk.END)
    url_entry.insert(0, filename)

def browse_directory():
    """Opens directory dialog for save path."""
    directory = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(0, directory)

def run_gui():
    """Launches the GUI."""
    global root, url_entry, save_path_entry, progress_bar, progress_label
    root = tk.Tk()
    root.title("Yank - YouTube Downloader")

    tk.Label(root, text="Enter YouTube URL or select a text file:").pack()
    url_entry = tk.Entry(root, width=50)
    url_entry.pack()
    tk.Button(root, text="Browse", command=browse_file).pack()

    tk.Label(root, text="Select save location:").pack()
    save_path_entry = tk.Entry(root, width=50)
    save_path_entry.pack()
    tk.Button(root, text="Browse", command=browse_directory).pack()

    tk.Label(root, text="Select video format:").pack()
    format_var = tk.StringVar(value=DEFAULT_FORMAT)
    tk.OptionMenu(root, format_var, "mp4", "mkv", "webm").pack()

    audio_only_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Audio Only", variable=audio_only_var).pack()

    subtitles_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download Subtitles", variable=subtitles_var).pack()

    thumbnail_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download Thumbnail", variable=thumbnail_var).pack()

    progress_label = tk.Label(root, text="")
    progress_label.pack()
    progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
    progress_bar.pack_forget()

    def on_download():
        """Handles download button click."""
        progress_bar["value"] = 0
        progress_bar.pack()

        input_source = url_entry.get()
        save_path = save_path_entry.get() or DEFAULT_SAVE_PATH
        format_choice = format_var.get()
        audio_only = audio_only_var.get()
        subtitles = subtitles_var.get()
        download_thumbnail = thumbnail_var.get()

        if os.path.isfile(input_source):
            with open(input_source, "r") as file:
                links = [line.strip() for line in file.readlines() if line.strip()]
        else:
            links = [input_source]

        threading.Thread(target=process_input, args=(links, save_path, format_choice, audio_only, subtitles, download_thumbnail), daemon=True).start()

    tk.Button(root, text="Download", command=on_download).pack()
    root.mainloop()

def run_cli(args):
    """Runs CLI mode."""
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
    """Parses arguments and runs CLI or GUI."""
    parser = argparse.ArgumentParser(description="Yank - YouTube Video Downloader")
    parser.add_argument('input', nargs='?', default=None, help="YouTube URL or text file path")
    parser.add_argument('--save_path', default=DEFAULT_SAVE_PATH, help="Directory to save videos")
    parser.add_argument('--format', choices=['mp4', 'mkv', 'webm'], default=DEFAULT_FORMAT, help="Video format")
    parser.add_argument('--audio_only', action='store_true', help="Download audio only")
    parser.add_argument('--subtitles', action='store_true', help="Download subtitles")
    parser.add_argument('--thumbnail', action='store_true', help="Download thumbnail")

    args = parser.parse_args()
    if args.input:
        run_cli(args)
    else:
        run_gui()

if __name__ == "__main__":
    main()
