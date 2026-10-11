🎮 Eaglercraft Launcher

A simple local launcher for Eaglercraft — run any version right in your browser or in a native window.

⚠️ DISCLAIMER

THIS IS NOT AN OFFICIAL MINECRAFT PRODUCT.
NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.

This project is not affiliated with Mojang, Microsoft, or the original Eaglercraft by LAX1DUDE. It does not distribute any Minecraft game files or assets. It only serves locally-stored HTML files through a local HTTP server.

For personal, educational, and non-commercial use only.
No ads. No monetization.

────────────────────────────────────────

📖 ABOUT

Eaglercraft Launcher runs Eaglercraft versions locally with one click. It starts a local HTTP server and serves the game.

Three interfaces:
- CLI (main.py) — simple text menu
- GUI (mainGUI.py) — dark-themed window, opens game in browser
- GUI Native (mainGUIweb.py) — same window, opens game in a separate native window via pywebview

All support English and Russian.

────────────────────────────────────────

✨ FEATURES

- Versions: 1.3 beta, 1.5.2, 1.7.3 beta, Indev, Scratch, 1.8.8, 1.12.2, 26.2
- WASM / JS loaders for 1.8.8 and 1.12.2
- English & Russian UI
- Auto-opens browser (CLI / GUI) or native window (GUI Native)
- No dependencies for CLI and GUI — pure Python standard library
- pywebview required for GUI Native (installed via install.cmd)

────────────────────────────────────────

📋 REQUIREMENTS

- Python 3.10 or newer
- Windows 10 / 11
- Any modern browser
- ~250 MB disk space for game files

For GUI Native (mainGUIweb.py):
- pywebview (install via install.cmd)
- Microsoft Edge WebView2 (usually pre-installed on Windows 10/11)

────────────────────────────────────────

🚀 QUICK START

1. Extract the RAR archive.
2. Run install.cmd (installs pywebview for GUI Native).
3. Run start.cmd and choose which launcher to start.
4. Launch and play.

────────────────────────────────────────

🎮 USAGE

Option 1 — double-click start.cmd, pick 1, 2 or 3.

Option 2 — run manually:

    python main.py          (CLI)
    python mainGUI.py       (GUI — opens in browser)
    python mainGUIweb.py    (GUI Native — opens in a separate window)

Then choose language, version, loader (if needed) — the game opens automatically.

To stop: close window or press Enter.

────────────────────────────────────────

📁 STRUCTURE

    main.py            # CLI launcher
    mainGUI.py         # GUI launcher (Tkinter) — browser
    mainGUIweb.py      # GUI launcher (Tkinter + pywebview) — native window
    start.cmd          # Windows menu
    install.cmd        # Installs pywebview (for GUI Native)
    versions/          # game files (NOT included)

────────────────────────────────────────

⚖️ LICENSE

MIT — applies only to launcher code.

NOT covered by MIT:
- Minecraft (Mojang / Microsoft)
- Eaglercraft (LAX1DUDE)
- Game files in versions/

────────────────────────────────────────

🙏 CREDITS

- Eaglercraft by LAX1DUDE
- Minecraft by Mojang / Microsoft
- Launcher code by me (GUI and GUI Native with AI assistance)
- Design inspired by Catppuccin

────────────────────────────────────────

Made with ❤️ and Python
