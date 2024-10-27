"""random word"""
import random
def random_word(wordlist):
    """random word from word list"""
    word_key = list(wordlist.keys())
    random_wordlist = {}
    while word_key:
        random_word = random.choice(word_key)
        random_wordlist[random_word] = wordlist[random_word]
        word_key.remove(random_word)
    return random_wordlist
