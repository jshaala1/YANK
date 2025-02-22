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

### **Option 1: Standalone .exe (Windows Only - No Python Required)**  
You can easily download the `.exe` file and run it without needing Python or any dependencies. 

#### How to Use:  
1. Download the `.exe` file (provided in the release).  
2. Double-click the file to launch the program.  
3. Enter a YouTube URL (or choose a CSV file with multiple URLs).  
4. Select your desired video format, audio only option, subtitles, and thumbnail download options.  
5. Click "Download" and let the tool grab the video for you.

### **Option 2: Standalone Executable for Linux**  
For Linux users, you can download the precompiled `.exe` file or build it from source as described below.  

- **Run the Linux binary**: Download the executable for Linux from the releases section and run it directly, no need for Python.

#### How to Use:  
1. Download the Linux `.exe` (or `.bin` for Linux) file.  
2. Mark the file as executable:  
   ```bash
   chmod +x YANK
   ```  
3. Run the file directly:  
   ```bash
   ./YANK
   ```

### **Option 3: Command-Line Usage (Requires Python)**  
If you prefer running the tool from the command line, you can clone the repository and use it via Python. 

1. **Install Dependencies**  
   - Clone this repository:  
     ```bash
     git clone https://github.com/jshaala1/YANK.git
     ```  
   - Navigate into the project folder:  
     ```bash
     cd YANK
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
    - Launch GUI 
     ```bash
     python YANK.py 
     ```
     Example:  
     ```bash
     python YANK.py https://youtube.com/xyz --save_path "C:\Downloads" --format mp4 --audio_only --subtitles --thumbnail
     ```

---

## **How to Build (For Developers)**  
YANK was built using **Python** and **yt-dlp**, and you can modify or extend the functionality.

### Steps to Build:  
1. **Clone the repository**  
   - Clone the repository to your local machine:  
     ```bash
     git clone https://github.com/jshaala1/YANK.git
     ```  
   - Navigate to the cloned folder:  
     ```bash
     cd YANK
     ```

2. **Create and Activate a Virtual Environment**  
   - Create a virtual environment:  
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:  
     - On **Windows**:  
       ```bash
       .\venv\Scripts\activate
       ```  
     - On **macOS/Linux**:  
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**  
   - Install the required Python dependencies:  
     ```bash
     pip install -r requirements.txt
     ```

4. **Build the Standalone Executable for Windows**  
   - Install **PyInstaller** (if not already installed):  
     ```bash
     pip install pyinstaller
     ```
   - Build the executable using PyInstaller:  
     ```bash
     pyinstaller --onefile --windowed --hidden-import yt_dlp --hidden-import tkinter YANK.py
     ```

   After building, the `.exe` file will be located in the `dist` folder.

5. **Build the Standalone Executable for Linux**  
   To build a Linux binary, follow these instructions:

   - Ensure that you have **PyInstaller** installed:  
     ```bash
     pip install pyinstaller
     ```

   - Build the executable:  
     ```bash
     pyinstaller --onefile YANK.py
     ```

   The `.exe` or `.bin` file for Linux will be located in the `dist` folder.

6. **(Optional) Create a Windows Installer**  
   If you want to create a more polished installer for Windows, you can use **Inno Setup** or another installer tool to bundle the executable into an installer.

7. **Deactivate the Virtual Environment**  
   - When you're done building, deactivate the virtual environment:  
     ```bash
     deactivate
     ```

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
