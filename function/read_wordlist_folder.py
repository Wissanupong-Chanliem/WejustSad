import os
def read_wordlist_dir():
    text_files = {}
    for x in os.listdir("static/wordlist"):
        if x.endswith(".txt"):
            # Prints only text file present in My Folder
            text_files[x.rstrip(".txt")] = "static/wordlist/" + x
    return text_files