while wordlist:
        random_word = random.choice(word_key)
        print(random_word)
        wordlist.pop(random_word)
        word_key.remove(random_word)