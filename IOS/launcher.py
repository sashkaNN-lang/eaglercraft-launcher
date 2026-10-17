import os
import sys
import subprocess
import urllib.request
import zipfile
import shutil

TARGET_DIR = os.path.expanduser("~/Documents/eaglercraft-launcher")
ZIP_URL = "https://github.com/sashkaNN-lang/eaglercraft-launcher/releases/latest/download/eaglercraft-launcher.zip"
ZIP_PATH = os.path.join(TARGET_DIR, "temp.zip")


def find_main_py(folder):
    for root, _, files in os.walk(folder):
        if "main.py" in files:
            return root


def download_and_extract():
    print("Downloading...")
    os.makedirs(TARGET_DIR, exist_ok=True)
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)

    print("Extracting...")
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall(TARGET_DIR)
    os.remove(ZIP_PATH)

    main_dir = find_main_py(TARGET_DIR)
    if not main_dir:
        print("main.py not found")
        sys.exit(1)

    if main_dir != TARGET_DIR:
        for item in os.listdir(main_dir):
            src, dst = os.path.join(main_dir, item), os.path.join(TARGET_DIR, item)
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            elif os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
        for root, _, _ in os.walk(TARGET_DIR, topdown=False):
            if root != TARGET_DIR and not os.listdir(root):
                os.rmdir(root)


if __name__ == "__main__":
    main_script = os.path.join(TARGET_DIR, "main.py")
    if not os.path.exists(main_script):
        download_and_extract()
    print(f"Done. main.py is at: {main_script}")
