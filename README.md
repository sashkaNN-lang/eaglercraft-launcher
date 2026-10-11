🎮 Eaglercraft Launcher

A simple local launcher for Eaglercraft — run any version right in your browser.

⚠️ DISCLAIMER

THIS IS NOT AN OFFICIAL MINECRAFT PRODUCT.
NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.

This project is not affiliated with Mojang, Microsoft, or the original Eaglercraft by LAX1DUDE. It does not distribute any Minecraft game files or assets. It only serves locally-stored HTML files through a local HTTP server.

For personal, educational, and non-commercial use only.
No ads. No monetization.

────────────────────────────────────────

📖 ABOUT

Eaglercraft Launcher runs Eaglercraft versions locally with one click. It starts a local HTTP server, opens your browser, and serves the game.

Two interfaces:
- CLI (main.py)
- GUI (mainGUI.py)

Both support English and Russian.

────────────────────────────────────────

✨ FEATURES

- Versions: 1.3 beta, 1.5.2, 1.7.3 beta, 1.8.8, 1.12.2, 26.2
- WASM / JS loaders for 1.8.8 and 1.12.2
- English & Russian UI
- Auto-opens browser
- No dependencies — pure Python standard library

────────────────────────────────────────

📋 REQUIREMENTS

- Python 3.10 or newer
- Windows 10 / 11
- Any modern browser
- ~250 MB disk space for game files

────────────────────────────────────────

🎮 USAGE

Option 1 — double-click start.cmd, pick 1 or 2.

Option 2 — run manually:

    python main.py       (CLI)
    python mainGUI.py    (GUI)

Then choose language, version, loader (if needed) — browser opens automatically.

To stop: close window or press Enter.

────────────────────────────────────────

📁 STRUCTURE

    main.py            # CLI launcher
    mainGUI.py         # GUI launcher (Tkinter)
    start.cmd          # Windows menu
    README.md
    CHANGELOG.md
    LICENSE
    versions/          # game files (NOT included)

────────────────────────────────────────

📜 CHANGELOG

Latest — 0.1.1 Alpha (2026-10-11):
- Added GUI launcher (mainGUI.py)
- Updated start.cmd
- Published on GitHub

Full history: see CHANGELOG.md

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
- Launcher code by me (GUI with AI assistance)
- Design inspired by Catppuccin

────────────────────────────────────────

Made with ❤️ and Python
