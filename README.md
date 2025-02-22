# YANK: Video Downloader

## **Overview**  
YANK is a **wrapper** around the powerful [yt-dlp](https://github.com/yt-dlp/yt-dlp) library, designed to provide a **clean, straightforward way** to download videos from YouTube and other supported platforms.

Forget sketchy websites, intrusive ads, and confusing options—this app does the heavy lifting for you with just a few clicks. **No nonsense. No hassle.**

---

## **Features**  
- **Download videos** from YouTube and other supported websites.  
- Choose your **video format** (e.g., `mp4`, `webm`, `mkv`).  
- Save videos directly to your desired location.  
- **Download audio only** with formats like `mp3` or `m4a`.  
- **Download subtitles** in the language of your choice (e.g., English).  
- **Download thumbnails** alongside your videos.  
- **Command-line or GUI** options for easy usage.  
- Uses the powerful **yt-dlp** library, an **improved version** of youtube-dl.  
- Avoid sketchy websites and pop-ups—just clean video downloads.

---

## **How It Works**  
YANK wraps the **yt-dlp** library, one of the most powerful open-source tools for downloading videos. yt-dlp is faster, more reliable, and more feature-rich than other similar tools.

We’ve built an easy-to-use interface on top of it so you don’t have to worry about using the command line (unless you prefer it). Whether you're using the GUI or running it from the terminal, the tool gives you clean video downloads without the BS.

---

## **Installation and Usage**

### **Option 1: Standalone .exe (No Python Required)**  
You can easily download the `.exe` file and run it without needing Python or any dependencies. 

#### How to Use:  
1. Download the `.exe` file (provided).  
2. Double-click the file to launch the program.  
3. Enter a YouTube URL (or choose a CSV file with multiple URLs).  
4. Select your desired video format, audio only option, subtitles, and thumbnail download options.  
5. Click "Download" and let the tool grab the video for you.

### **Option 2: Command-Line Usage (Requires Python)**  
If you prefer running the tool from the command line, you can clone the repository and use it via Python. 

1. **Install Dependencies**  
   - Clone this repository:  
     ```bash
     git clone https://github.com/jshaala1/YANK/tree/main
     ```  
   - Install Python dependencies:  
     ```bash
     pip install -r requirements.txt
     ```

2. **Run from Command Line**  
   - Usage:  
     ```bash
     python YANK.py <YouTube URL or path to CSV file with URLs> --save_path <Optional: destination folder> --format <Optional: mp4, mkv, webm> --audio_only --subtitles --thumbnail
     ```
     Example:  
     ```bash
     python YANK.py https://youtube.com/xyz --save_path "C:\Downloads" --format mp4 --audio_only --subtitles --thumbnail
     ```

---

## **How to Build (For Developers)**  
YANK was built using **Python** and **yt-dlp**, and you can modify or extend the functionality.

### Steps to Build:  
1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Build the standalone executable using **PyInstaller**:  
   ```bash
   pyinstaller --onefile --windowed --hidden-import yt_dlp --hidden-import tkinter YANK.py
   ```
   After building, you’ll find the `.exe` in the `dist` folder.  
4. For extra polish, consider creating a Windows installer using **Inno Setup**.

---

## **Why This Tool?**  
Many video download websites are **sketchy**, full of ads, pop-ups, or worse—malware. YANK was created to **avoid all that** and give you a simple, safe way to download videos.

- **No fake "Download" buttons**  
- **No pop-ups or redirects**  
- **No sketchy websites**  
- **No risk of malware**

Just clean, reliable video downloads—without the hassle.

---

## **Credits**  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing the core video download functionality.  
- [PyInstaller](https://www.pyinstaller.org/) for creating the standalone `.exe` file.  

---

## **Disclaimer**  
This tool is **for educational purposes only**. Please ensure you respect copyright and intellectual property rights when using this tool. Downloading videos from YouTube and other platforms may be subject to the **terms of service** of the respective websites. Always ensure you have permission to download content.

---

