import os
import subprocess
import sys
import urllib.request

# Function to check if Python is installed
def is_python_installed():
    try:
        subprocess.run(["python", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to download Python installer
def download_python():
    python_url = "https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe"
    installer_path = "python_installer.exe"
    print("Downloading Python...")
    urllib.request.urlretrieve(python_url, installer_path)
    print("Download complete! Please install Python manually and restart the script.")
    os.startfile(installer_path)
    sys.exit(1)

# Check Python
if not is_python_installed():
    download_python()

# Create virtual environment
if not os.path.exists("venv"):
    print("Creating virtual environment...")
    subprocess.run(["python", "-m", "venv", "venv"])

# Activate virtual environment
venv_python = os.path.join("venv", "Scripts", "python.exe")

# Upgrade pip
subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])

# Install dependencies
try:
    subprocess.run([venv_python, "-c", "import curses"], check=True)
except subprocess.CalledProcessError:
    print("Installing windows-curses...")
    subprocess.run([venv_python, "-m", "pip", "install", "windows-curses"])

# Run the game
print("Starting game...")
subprocess.run(["start", "cmd", "/k", f"mode con: cols=80 lines=40 && {venv_python} main.py"], shell=True)
