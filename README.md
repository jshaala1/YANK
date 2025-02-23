# YANK: Youtube Video Downloader

## **Overview**  
YANK is a **wrapper** around the powerful [yt-dlp](https://github.com/yt-dlp/yt-dlp) library, designed to provide a **clean, straightforward way** to download videos from YouTube and other supported platforms.

Forget sketchy websites, intrusive ads, and confusing options—this app does the heavy lifting for you with just a few clicks. **No nonsense. No hassle.**

---

## **Features**  
- **Download videos** from YouTube and other supported websites.  
- Choose your **video format** (e.g., `mp4`, `webm`, `mkv`).  
- Save videos directly to your desired location.  
- **Download audio only** in formats like `mp3` or `m4a`.  
- **Download subtitles** in the language of your choice.  
- **Download thumbnails** alongside your videos.  
- **Command-line or GUI** options for easy usage.  
- Uses the powerful **yt-dlp** library, an **improved version** of youtube-dl.  
- Avoid sketchy websites and pop-ups—just clean video downloads.

---

## **How It Works**  
YANK wraps the **yt-dlp** library, one of the most powerful open-source tools for downloading videos. We’ve built an easy-to-use interface on top of it, making it accessible for both GUI and CLI users.

---

## **Installation and Usage**

### **Option 1: Standalone Executable (Windows & Linux)**  
YANK provides prebuilt executables for Windows and Linux, allowing you to run the tool without installing Python or dependencies.

#### How to Use:  
1. Download the `.exe` (Windows) or `.bin` (Linux) file from the releases section.  
2. **Windows:** Double-click to launch.  
   **Linux:** Mark as executable and run:
   ```bash
   chmod +x YANK
   ./YANK
   ```
3. Enter a YouTube URL (or choose a text file with multiple URLs).  
4. Select your desired options and click **Download**.

### **Option 2: Command-Line Usage (Requires Python)**  
For users who prefer the command line, YANK can be run directly via Python.

#### Steps:
1. **Clone the Repository & Install Dependencies**
   ```bash
   git clone https://github.com/jshaala1/YANK.git
   cd YANK
   pip install -r requirements.txt
   ```

2. **Ensure FFmpeg is Installed**
   - **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **macOS:**
     ```bash
     brew install ffmpeg
     ```
   - **Windows:** Download FFmpeg from [here](https://ffmpeg.org/download.html) and follow the installation guide.

3. **Run YANK**
   - **GUI Mode:**
     ```bash
     python YANK.py
     ```
   - **CLI Mode:**
     ```bash
     python YANK.py <YouTube URL or path to text file> --save_path <destination folder> --format <mp4, mkv, webm> --audio_only --subtitles --thumbnail
     ```
     Example:
     ```bash
     python YANK.py https://youtube.com/xyz --save_path "C:\Downloads" --format mp4 --audio_only --subtitles --thumbnail
     ```

---

## **How to Build (For Developers)**  
YANK was built using **Python** and **yt-dlp**, and you can modify or extend its functionality.

### **Building Standalone Executable**
1. **Clone the Repository & Set Up Virtual Environment**
   ```bash
   git clone https://github.com/jshaala1/YANK.git
   cd YANK
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Build Executable**
   - **Windows:**
     ```bash
     pyinstaller --onefile --windowed --hidden-import yt_dlp --hidden-import tkinter YANK.py
     ```
   - **Linux:**
     ```bash
     pyinstaller --onefile YANK.py
     ```
   The output executable will be located in the `dist` folder.

### **(Optional) Embed FFmpeg into Executable**
For a fully self-contained version, you can bundle FFmpeg into the standalone executable:
- Download a static build of FFmpeg from [here](https://ffmpeg.org/download.html).
- Modify the PyInstaller build command to include the FFmpeg binary:
  ```bash
  pyinstaller --onefile --windowed --add-binary "path/to/ffmpeg;ffmpeg" --hidden-import yt_dlp --hidden-import tkinter YANK.py
  ```
  This ensures that FFmpeg is embedded within the executable, so users don’t need to install it separately.

---

## **Why Use YANK?**  
Many video download websites are **sketchy**, full of ads, pop-ups, or worse—malware. YANK was created to **avoid all that** and provide a simple, safe way to download videos.

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

