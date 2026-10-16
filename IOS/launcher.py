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
    for root, dirs, files in os.walk(folder):
        if "main.py" in files:
            return root
    return None


def download_and_extract():
    print("Downloading...")
    os.makedirs(TARGET_DIR, exist_ok=True)

    try:
        urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)
    except Exception as e:
        print(f"Download failed: {e}")
        sys.exit(1)

    print("Extracting...")
    try:
        with zipfile.ZipFile(ZIP_PATH, "r") as z:
            z.extractall(TARGET_DIR)
    except Exception as e:
        print(f"Extraction failed: {e}")
        sys.exit(1)

    os.remove(ZIP_PATH)

    main_dir = find_main_py(TARGET_DIR)
    if not main_dir:
        print("main.py not found after extraction")
        sys.exit(1)

    if main_dir != TARGET_DIR:
        print(f"Moving files from {main_dir} to {TARGET_DIR}...")
        for item in os.listdir(main_dir):
            src = os.path.join(main_dir, item)
            dst = os.path.join(TARGET_DIR, item)
            if os.path.exists(dst):
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                else:
                    os.remove(dst)
            shutil.move(src, dst)

        for root, dirs, files in os.walk(TARGET_DIR, topdown=False):
            if root != TARGET_DIR and not os.listdir(root):
                os.rmdir(root)


def main():
    main_script = os.path.join(TARGET_DIR, "main.py")

    if os.path.exists(main_script):
        print("Files already in place. Running main.py...")
    else:
        print("No files found. Downloading...")
        download_and_extract()

    subprocess.run([sys.executable, main_script])


if __name__ == "__main__":
    main()
