from tkinter import filedialog as fd
import shutil
def open_file_selection():
    file = fd.askopenfile()
    # do some file copying magic
    file.close()