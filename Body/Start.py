import os
import subprocess

Project_Path = os.path.dirname(__file__)

def lang_var():
    return open(rf"{Project_Path}\lang_var.txt", 'r', encoding='utf-8').read() 

if lang_var() == "ru":
    subprocess.Popen(['python', r".\Body\RemoteRU.py"])

elif lang_var() == "en":
    subprocess.Popen(['python', r".\Body\RemoteEN.py"])
