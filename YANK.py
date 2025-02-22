import os
import sys
import argparse
import re
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


# global variables for progress bar
progress_bar = None
progress_label = None
root = None  # reference for the root window


def is_valid_youtube_url(url):
    """validates if the given URL is a valid YouTube URL."""
    youtube_regex = (
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|playlist\?list=|(?:v|e(?:mbed)?)\S*?[?&]v=)[a-zA-Z0-9_-]+'
    )
    return re.match(youtube_regex, url) is not None


def progress_hook(d):
    """updates the progress bar during download."""
    if d['status'] == 'downloading' and progress_bar:
        try:
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', d.get('total_bytes_estimate', 1))
            percentage = int((downloaded / total) * 100)
            progress_bar["value"] = percentage
            progress_label.config(text=f"Downloading... {percentage}%")
            root.update_idletasks()
        except Exception as e:
            print(f"Error updating progress bar: {e}")


def download_video(video_url, save_path=".", format_choice="webm", audio_only=False, subtitles=False, download_thumbnail=False):
    """downloads the video with specified options."""
    try:
        ydl_opts = {
            'format': f'bestvideo[ext={format_choice}]+bestaudio[ext={format_choice}]/best[ext={format_choice}]',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook]
        }

        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]

        if subtitles:
            ydl_opts['writesubtitles'] = True
            ydl_opts['subtitleslangs'] = ['en']

        if download_thumbnail:
            ydl_opts['writethumbnail'] = True

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            messagebox.showinfo("Success", f"Downloaded: {info_dict['title']}")

        # reset progress bar
        progress_bar["value"] = 0
        progress_label.config(text="Download Complete!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def process_input(video_urls, save_path, format_choice, audio_only, subtitles, download_thumbnail):
    """processes the video URLs and starts download."""
    for link in video_urls:
        download_video(link, save_path, format_choice, audio_only, subtitles, download_thumbnail)


def browse_file():
    """opens file dialog to select CSV file."""
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    url_entry.delete(0, tk.END)
    url_entry.insert(0, filename)


def browse_directory():
    """opens directory dialog to select save path."""
    directory = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(0, directory)


def run_gui():
    """launches the GUI."""
    global progress_bar, progress_label, root

    root = tk.Tk()
    root.title("YANK")

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

    audio_only_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Audio only", variable=audio_only_var).pack()

    subtitles_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download subtitles", variable=subtitles_var).pack()

    thumbnail_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Download thumbnail", variable=thumbnail_var).pack()

    # progress bar UI: initially hidden
    progress_label = tk.Label(root, text="")
    progress_label.pack()

    progress_bar = ttk.Progressbar(root, length=300, mode="determinate")
    progress_bar.pack_forget()  # initially hide the progress bar

    def on_download():
        """handles download when button is clicked."""
        # make progress bar visible
        progress_bar["value"] = 0
        progress_bar.pack()

        input_source = url_entry.get()
        save_path = save_path_entry.get() or "."
        format_choice = format_var.get()
        audio_only = audio_only_var.get()
        subtitles = subtitles_var.get()
        download_thumbnail = thumbnail_var.get()

        if os.path.isfile(input_source):
            with open(input_source, "r") as file:
                links = [line.strip() for line in file.readlines() if line.strip()]
        else:
            links = [input_source]

        process_input(links, save_path, format_choice, audio_only, subtitles, download_thumbnail)

    tk.Button(root, text="Download", command=on_download).pack()
    root.mainloop()


def run_cli(args):
    """runs the CLI mode."""
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
    """parses arguments and runs CLI or GUI."""
    parser = argparse.ArgumentParser(
        description="YANK a tool to download youtube videos via url or csv with options"
    )
    parser.add_argument('input', nargs='?', default=None, help="youtube URL or path to csv")
    parser.add_argument('--save_path', default=".", help="directory to save videos")
    parser.add_argument('--format', choices=['mp4', 'mkv', 'webm'], default='webm', help="video format")
    parser.add_argument('--audio_only', action='store_true', help="download audio only")
    parser.add_argument('--subtitles', action='store_true', help="download subtitles")
    parser.add_argument('--thumbnail', action='store_true', help="download thumbnail")

    # show help if --help or -h is passed
    args = parser.parse_args()

    if args.input:
        run_cli(args)
    else:
        run_gui()


if __name__ == "__main__":
    main()
