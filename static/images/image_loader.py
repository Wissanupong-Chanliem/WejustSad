"""File Converter for Development"""
import subprocess

import glob
def convert():
    for image in glob.glob("static\\images\\*.*",recursive=True):
        subprocess.Popen(["./cimg",f"{image}",f"{image.replace(".png",".webp")}"])
convert()