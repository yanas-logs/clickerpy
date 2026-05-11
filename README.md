# Clickerpy

Clickerpy is a lightweight, Python-based desktop application designed for automated mouse clicking. Built with `tkinter` and `PyAutoGUI`, it provides a clean and user-friendly interface to manage click intervals, click types, and multitasking features.

---

## ✨ Features

* **Customizable Intervals**
  Set the delay between clicks in seconds.

* **Multiple Click Modes**

  * **Default** → Consistent clicking based on your configured interval.
  * **Custom** → Burst clicking mode (3 clicks per second).
  * **Randomize** → Simulates human-like clicking with random intervals between 5–15 seconds.

* **Visual Timer**
  Real-time timer display in `MM.SS.ms` format.

* **Test Module**
  Includes a **Test Click Counter** to verify click speed and accuracy.

* **Stay on Top**
  Lock the window above other applications for easier multitasking.

* **Theme Support**
  Switch between **Light** and **Dark** modes.

* **Responsive UI**
  Uses multi-threading to keep the interface responsive while the auto-clicker is running.

---

## 📦 Prerequisites

Before installing Clickerpy, make sure the following are installed on your system:

* **Python 3.12** *(recommended for best compatibility)*
* **Tkinter**

  * Usually included with Python on **Windows**
  * On **Linux**, you may need to install it manually

---

## 🖥️ Supported Platforms

Clickerpy supports multiple operating systems:

* ✅ Windows
* ✅ Linux

> **Note:** PyAutoGUI and tkinter are supported on Linux, but some desktop environments may require additional permissions or packages.

---

## 🚀 Installation

Follow these steps to set up Clickerpy on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yanas-logs/clickerpy.git
cd clickerpy
```

### 2. Create a Virtual Environment

Using a virtual environment is highly recommended to avoid dependency conflicts.

```bash
# Using Python Launcher
py -3.12 -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

#### Windows (CMD)

```cmd
venv\Scripts\activate
```

#### Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Linux Additional Setup (Optional)

Some Linux distributions may require additional tkinter packages.

#### Debian / Ubuntu

```bash
sudo apt update
sudo apt install python3-tk
```

#### Arch Linux

```bash
sudo pacman -S tk
```

#### Fedora

```bash
sudo dnf install python3-tkinter
```

---

## ▶️ Usage

Run the application using:

```bash
python main.py
```

---

## 🎮 Controls

| Button            | Function                                    |
| ----------------- | ------------------------------------------- |
| **Start**         | Begins the auto-clicking process and timer  |
| **Stop**          | Stops the current clicking process          |
| **Reset**         | Resets the timer and stops the clicker      |
| **Lock / Unlock** | Toggles the window's “Always on Top” status |
| **Settings Menu** | Configure click intervals and click modes   |

---

## ⚠️ Safety Note

If the script behaves unexpectedly, move your mouse cursor to the **top-left corner (0,0)** of your screen.

This triggers the built-in **PyAutoGUI fail-safe** and immediately stops the program.

---

## 🛠️ Built With

* Python
* tkinter
* PyAutoGUI
* threading

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.
