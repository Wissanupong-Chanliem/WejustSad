def sort_word(word,row_size):
    now = row_size
    new_word = []
    temp = []
    for w,lenght in word.items():
        if now-lenght<0:
            new_word.append(temp)
            temp = [w]
            now = row_size-lenght
        else:
            temp.append(w)
            now -= lenght
    if temp:
        new_word.append(temp)
    return new_word
