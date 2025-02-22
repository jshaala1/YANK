# Video Downloader: A Clean, Simple Tool for Downloading YouTube Videos

## **Overview**  
This tool is a **wrapper** around the powerful [yt-dlp](https://github.com/yt-dlp/yt-dlp) library, designed to give you a **clean, straightforward way** to download videos from YouTube. 

Forget the sketchy download websites, intrusive ads, and confusing options—this app does the heavy lifting for you with just a few clicks. **No nonsense. No hassle.**

---

## **Features**  
- **Download videos** from YouTube and other supported websites. 
- Choose your **video format** (e.g., `mp4`, `webm`, `mkv`). 
- Save videos directly to your desired location. 
- **Download audio only** with formats like `mp3` or `m4a`. 
- **Download subtitles** in the language of your choice (e.g., English). 
- **Download thumbnails** alongside your videos. 
- **Command-line or GUI** options for easy usage. 
- Uses the robust **yt-dlp** library, which is a **faster, improved version** of youtube-dl. 
- No need to visit sketchy websites or deal with pop-ups. Just clean video downloads.

---

## **How It Works**  
This tool works by wrapping the **yt-dlp** library—one of the most powerful, open-source tools for downloading videos from a variety of sources. It’s faster, more reliable, and more feature-rich than other similar tools.

We’ve built an easy-to-use interface on top of it, so you don’t have to interact with the command-line yourself (unless you want to). Whether you're using the GUI or running it via the command line, the functionality remains the same: clean video downloads without the BS.

---

## **Installation and Usage**

### **Option 1: Standalone .exe (No Python Required)**  
You can simply download the `.exe` file and run it without needing to install Python or any dependencies. 

#### How to Use:  
1. Download the `.exe` file (provided). 
2. Double-click the file to launch the program. 
3. Enter a YouTube URL (or choose a CSV file with multiple URLs). 
4. Select your desired video format, audio only option, subtitle download, and thumbnail download. 
5. Click "Download" and let the tool grab the video for you. 

### **Option 2: Command-Line Usage (Requires Python)**  
If you prefer to run the tool from the command line, you can clone this repository and use it via Python. 

1. **Install Dependencies** 
   - Clone this repository: 
     ```bash
     git clone https://github.com/yourusername/VideoDownloader.git
     ```
   - Install Python dependencies: 
     ```bash
     pip install -r requirements.txt
     ```

2. **Run from Command Line** 
   - Usage:
     ```bash
     python your_script.py <YouTube URL or path to CSV file with URLs> --save_path <Optional: destination folder> --format <Optional: mp4, mkv, webm> --audio_only --subtitles --thumbnail
     ```
     Example: 
     ```bash
     python your_script.py https://youtube.com/xyz --save_path "C:\Downloads" --format mp4 --audio_only --subtitles --thumbnail
     ```

---

## **How to Build (For Developers)**  
This project was built using **Python** and **yt-dlp**, and you can also modify or extend the functionality. 

### Steps to Build:  
1. Clone the repository. 
2. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```
3. Build the standalone executable using **PyInstaller**:
   ```bash
   pyinstaller --onefile --windowed --hidden-import yt_dlp --hidden-import tkinter your_script.py
   ```
   After building, you’ll find the `.exe` in the `dist` folder. 
4. For extra polish, consider creating a Windows installer using **Inno Setup**. 

---

## **Why This Tool?**  
Many video download websites are **sketchy**, full of ads and pop-ups. Some even contain malware or malicious software. This tool was made to **avoid all that BS**—just a simple, easy way to download videos with no distractions or dangers.

- **No more fake "Download" buttons** 
- **No more pop-ups or redirects** 
- **No more sketchy websites that might steal your data**
- **No more risk of malware**

Just clean, reliable video downloads—without the hassle.

---

## **Credits**  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing the core video download functionality. 
- [PyInstaller](https://www.pyinstaller.org/) for creating the standalone `.exe` file. 

---

## **Disclaimer**  
This tool is **for educational purposes only**. Please ensure that you respect copyright and intellectual property rights when using this tool. Downloading videos from YouTube and other platforms may be subject to **terms of service** of the respective websites. Always ensure you have permission to download content.

---

