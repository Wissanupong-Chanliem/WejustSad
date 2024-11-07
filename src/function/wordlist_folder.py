from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
import shutil
import os
from tkinter.messagebox import askyesno

def open_file_selection():
    file = fd.askopenfilename(initialdir="/", title="Select file", filetypes=[("Text Files","*.txt")])
    if not file:
        return
    if check_format(file):
        messagebox.showerror('Error', 'Error: ไฟล์ผิด format นะจ๊ะ อิอิ!\nFormat ที่ถูกต้อง:\nคำ = ความหมาย\nบรรทัดละ 1 คำ')
        return
    shutil.copy2(file,"wordlist")
    return os.path.basename(file).removesuffix(".txt")

def check_format(file:str):
    txt = open(file,"r",encoding="utf-8")
    check = 1
    for t in txt:
        check = 0
        if not " = " in t:
            return 1
        if t.count(" = ")>1:
            return 1
    if check:
        return 1
    return 0

def remove_wordlist(path:str):
    answer = askyesno(title='delete',message='จะลบจริงหรอจ๊ะ?')
    if os.path.exists(path) and answer:
        os.remove(path)
