def read_word_list(path):
    """read word list from txt file"""
    wordlist = {}
    txt = open(path,"r",encoding="utf-8")
    for t in txt:
        t = t.replace("\n","")
        t = t.split("=")
        wordlist[t[0]] = t[1]
    return wordlist

read_word_list("static\\wordlist\\pupe-word.txt")