# 🐍 Snake Game (Terminal Version)  

A simple **terminal-based Snake Game** built with **Python and curses**, compatible with **Windows, Linux, and macOS**.  
The game automatically sets up the required environment and runs in a properly sized terminal window.  

---

## 📌 Features  
✔ **Classic Snake Gameplay** – Move, eat food, and grow!  
✔ **One-Click Setup** – Just run `setup.exe`, and everything is installed & launched!  
✔ **Cross-Platform** – Works on **Windows, Linux, and macOS**  
✔ **Custom Terminal Size** – Ensures the correct game experience  

---

## 🎮 How to Play?  
- Use **Arrow Keys (<code>W</code>,<code>S</code>,<code>A</code>,<code>D</code>)** to move  
- Avoid crashing into **walls** or **yourself**  
- Eat **food** (🟢) to grow and increase score  
- Press **Q** to quit  

---

## 🚀 Installation & Setup  

### **🔹 Windows (Easiest Method - One Click)**  
1. **Double-click** on `setup.exe`  
2. It **automatically installs** everything needed and **runs the game**  

### **🔹 Alternative Windows Method (If `setup.exe` Fails)**  
1. Install **Python 3.x** if not installed ([Download Python](https://www.python.org/downloads/))  
2. Run `setup.bat`:  
   - **Right-click → Run as Administrator**  
   - This installs dependencies and starts the game.  

### **🔹 Linux/macOS**  
1. Open a terminal and **run**:  
   ```sh
   chmod +x setup.sh
   ./setup.sh
   ```
   - Installs **Python**, creates a virtual environment, and starts the game.  

---

## 🔧 **Technical Details**  

- The game uses **Python's `curses` module** for rendering.  
- On **Windows**, it installs **`windows-curses`** (since `curses` is not built-in).  
- The script **automatically downloads Python** if missing and sets up a virtual environment.  
- The game runs in a **new terminal with proper dimensions** for the best experience.  

---

## 🖥️ **Development & Customization**  

### **Run Without Setup**  
If you already have Python installed:  
```sh
python main.py
```

### **Modify Game Settings**  
- Open `main.py` and edit variables like **speed, colors, or controls**.  
- Change **terminal dimensions** in `setup.bat` (Windows) or `setup.sh` (Linux/macOS).  

---

## 🛠️ **Troubleshooting**  

### 🟢 **Game window closes instantly**  
- Run the script from the terminal:  
  ```sh
  python main.py
  ```
  This will show any errors.  

### 🔵 **EXE doesn’t work**  
- Run `setup.bat` manually or try the Python method.  

### 🔴 **Terminal not opening correctly on Linux/macOS**  
- Make sure you have **gnome-terminal**, **xterm**, or **konsole** installed.  
- If not, modify `setup.sh` to use your preferred terminal.  

---

## 🎯 **To-Do (Future Updates)**  
🔹 Add **difficulty levels**  
🔹 Implement **high scores**  
🔹 Add **sound effects**  

---

## 💖 **Contributors & Credits**  
- Developed by **_geekydev**  
- Uses **Python (`curses`)** for rendering  

🎮 Enjoy the game! 🚀