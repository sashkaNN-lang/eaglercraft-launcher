import os
import sys
import subprocess
import urllib.request
import zipfile

target_dir = os.path.expanduser("~/Documents/Eagler-craft launcher")
main_script = os.path.join(target_dir, "main.py")

if os.path.exists(main_script):
    print("The files are already in place. running main.py...")
else:
    print("There are no files. creating a folder and downloading...")
    os.makedirs(target_dir, exist_ok=True)
    
    zip_url = "https://github.com/sashkaNN-lang/eaglercraft-launcher/releases/latest/download/eaglercraft-launcher.zip"
    zip_path = os.path.join(target_dir, "temp.zip")
    
    urllib.request.urlretrieve(zip_url, zip_path)
    
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(target_dir)
    os.remove(zip_path)
    print("Done. launching main.py...")

subprocess.run([sys.executable, main_script])
