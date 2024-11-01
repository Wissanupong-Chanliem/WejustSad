from tkinter import filedialog as fd
import shutil
import os

def open_file_selection():
    file = fd.askopenfilename(initialdir="/", title="Select file", filetypes=[("Text Files","*.txt")])
    if check_format(file):
        print("Error")
        return
    shutil.copy2(file,"\\static\\wordlist" )

def check_format(file):
    txt = open(file,"r",encoding="utf-8")
    for t in txt:
        if not " = " in t:
            return 1
        if t.count(" = ")>1:
            return 
    return 0
    
