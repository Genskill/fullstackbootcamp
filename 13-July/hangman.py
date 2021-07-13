import random

# Dependency injection

def get_secret_word(word_file="/usr/share/dict/words", selector=random.choice):
    # 1. Each word should be atleast 5 letters
    # 2. No punctuation
    # 3. No proper nouns (first letter shouldn't be capital)
    good_words = []
    f = open(word_file)
    words = [x.strip() for x in f]
    f.close()
    for i in words:
        if (len(i) <= 4):
            continue
        if (not i.isalpha()):
            continue
        if (i.istitle()):
            continue
        if (i[0] == 'z'):
            continue
        good_words.append(i)


    return selector(good_words)
