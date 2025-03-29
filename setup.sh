#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3; then
    echo "Python not found! Installing..."
    if command_exists apt; then
        sudo apt update && sudo apt install -y python3 python3-venv
    elif command_exists brew; then
        brew install python3
    elif command_exists pacman; then
        sudo pacman -Sy python
    else
        echo "Package manager not supported! Install Python manually."
        exit 1
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found. Skipping."

# Open a new terminal with required dimensions and run the game
echo "Starting game..."
if command_exists gnome-terminal; then
    gnome-terminal --geometry=80x40 -- bash -c "source venv/bin/activate; python3 main.py; exec bash"
elif command_exists xfce4-terminal; then
    xfce4-terminal --geometry=80x40 --command "bash -c 'source venv/bin/activate; python3 main.py; exec bash'"
elif command_exists konsole; then
    konsole --geometry 80x40 --noclose -e "bash -c 'source venv/bin/activate; python3 main.py'"
elif command_exists xterm; then
    xterm -geometry 80x40 -e "bash -c 'source venv/bin/activate; python3 main.py; exec bash'"
else
    echo "No supported terminal found! Running in the current terminal..."
    python3 main.py
fi
