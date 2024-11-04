import os

def read_user_wordlist_dir():
    text_files = {}
    for x in os.listdir("wordlist"):
        if x.endswith(".txt"):
            text_files[x.removesuffix(".txt")] = "wordlist/" + x
    return text_files