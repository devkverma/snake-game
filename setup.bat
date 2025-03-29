@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found! Downloading...
    powershell -Command "& {Start-Process 'https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe' -Wait}"
    echo Please install Python manually and restart this script.
    pause
    exit /b
)

:: Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Ensure pip is updated
python -m pip install --upgrade pip

:: Check if curses is installed
python -c "import curses" 2>nul
if %errorlevel% neq 0 (
    echo Installing windows-curses...
    pip install windows-curses
)

:: Open a new terminal with correct size and run the game
echo Starting game...
start cmd /k "mode con: cols=100 lines=100 && call venv\Scripts\activate && python main.py"

exit /b
