# Eaglercraft Launcher — iOS

Launcher version for iPhone and iPad via the **a-Shell mini** app.

Main project (Windows / Mac / Linux / Android)

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
- Uses **one Shortcut** instead of `start.cmd`
- Works **only via CLI** (text menu)
- Opens the game in **Safari**

---

## ✨ FEATURES

- Versions: 1.3 beta, 1.5.2, 1.7.3 beta, Indev, Scratch, 1.8.8, 1.12.2, 26.2
- WASM / JS loaders for 1.8.8 and 1.12.2
- Interface in English and Russian
- Auto-open Safari
- Works fully on-device, no internet after installation
- **One-click launch** — no need for two shortcuts

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

### Step 2: Install the shortcut

Open the link:

**https://www.icloud.com/shortcuts/e86f2f580f6a46bfade6d2882599d3b9**

Tap **"Add Shortcut"**.

### Step 3: Run the shortcut

Open the shortcut from the Shortcuts app.

What happens automatically:
1. Checks if the launcher is installed.
2. If not — downloads the `.zip` of the latest release from GitHub.
3. Unpacks it to `~/Documents/eaglercraft-launcher`.
4. Runs `python main.py` in a-Shell mini.

*Note: the shortcut does NOT update the launcher automatically.*

### Step 4: Play

Choose language, version, and loader in the a-Shell menu.
The game opens in **Safari** automatically.

---

## 🔄 UPDATING (MANUAL)

To update to a new version, you need to delete the old files first.

**How to update:**
1. Open **a-Shell mini**.
2. Enter these commands one by one:

   rm -rf ~/Documents/eaglercraft-launcher
   rm -rf ~/Documents/myrepo

3. Close a-Shell mini.
4. Run the **shortcut** again.
5. It will automatically download the fresh version.
