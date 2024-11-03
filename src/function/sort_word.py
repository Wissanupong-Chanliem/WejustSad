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
    if temp:
        new_word.append(temp)
    for i in new_word:
        print(i)

sort_word({"word":24,"longergerger": 230,"longest":400,"loooooong":280,"short":30},300)