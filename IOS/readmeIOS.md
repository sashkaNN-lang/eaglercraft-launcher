# Eaglercraft Launcher — iOS

Launcher version for iPhone and iPad via the **a-Shell mini** app.

Main project (Windows).

---

## ⚠️ DISCLAIMER

THIS IS NOT AN OFFICIAL MINECRAFT PRODUCT.
NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.

This project is not affiliated with Mojang, Microsoft, or the original Eaglercraft by LAX1DUDE. It does not distribute Minecraft game files or resources. It only runs a local HTTP server and opens HTML files that are already on the user's device.

For personal, educational, and non-commercial use only.
No ads. No monetization.

---

## 📖 ABOUT THE PROJECT

The iOS version of Eaglercraft Launcher works via **a-Shell mini** — a terminal with Python for iPhone and iPad.

Since iOS has no `.cmd` or `tkinter`, this version:
- Uses **Shortcuts** instead of `start.cmd`
- Works **only via CLI** (text menu)
- Opens the game in **Safari**

---

## ✨ FEATURES

- Versions: 1.3 beta, 1.5.2, 1.7.3 beta, Indev, Scratch, 1.8.8, 1.12.2, 26.2
- WASM / JS loaders for 1.8.8 and 1.12.2
- Interface in English and Russian
- Auto-open Safari
- Update check
- Works fully on-device, no internet after installation

---

## 📋 REQUIREMENTS

- iPhone or iPad with **iOS 15+**
- **a-Shell mini** app (free on the App Store)
- **Shortcuts** app (built-in)
- ~250 MB free space
- Internet for the first installation

---

## 🚀 QUICK START

### Step 1: Install a-Shell mini

Download **a-Shell mini** from the App Store. It's free.

### Step 2: Install the launcher

Open the installation shortcut link:

**https://www.icloud.com/shortcuts/7b6d0e7233e044a4a9a6353c24aeadaa**

Tap **"Add Shortcut"** → run it.

The shortcut:
- Downloads the `.zip` of the latest release from GitHub
- Unpacks it to `~/Documents/eaglercraft-launcher`
- Prepares everything for launch

### Step 3: Launch the launcher

Open the launch shortcut link:

**https://www.icloud.com/shortcuts/3309b90b659f445ea9430e579ae33e98**

Tap **"Add Shortcut"** → run it.

The shortcut:
- Opens a-Shell mini
- Runs `python main.py`
- You choose language, version, loader
- Safari opens automatically with the game

### Step 4: Play

The game opens in **Safari**. Choose a version, play.

---

## 🎮 HOW TO PLAY

1. Run the **launch shortcut** (the second one)
2. A menu will appear in a-Shell:
