from tkinter import filedialog as fd
import shutil
import os

def open_file_selection():
    file = fd.askopenfilename(initialdir="/", title="Select file", filetypes=[("Text Files","*.txt")])
    # do some file copying magic
    # print(file.readlines())
    # target = 'import'
    # dir_parts = list(os.path.split(file))
    # target_dir = dir_parts[0] + target + '/' + dir_parts[1]
    if check_format(file):
        print("Error")
        return
    shutil.copy2(file,"C:\\Users\\User\\Documents\\งาน\\WejustSad\\static\\wordlist" )
    #file.close()

def check_format(file):
    txt = open(file,"r",encoding="utf-8")
    for t in txt:
        if not " = " in t:
            return 1
        if t.count(" = ")>1:
            return 
    return 0
    
open_file_selection()
