import hangman


def selector(l):
    return l[0]

def test_atleast_5_letters():
    f = open("/tmp/words.txt", "w")
    f.write("ruby\n")
    f.write("php\n")
    f.write("python\n")
    f.close()
    word = hangman.get_secret_word("/tmp/words.txt", selector)
    assert word == "python"

def test_no_punctuation():
    f = open("/tmp/words.txt", "w")
    f.write("ruby'\n")
    f.write("javascript!\n")
    f.write("python\n")
    f.write("#perl\n")
    f.close()
    word = hangman.get_secret_word("/tmp/words.txt", selector)
    assert word == "python"

def test_no_proper_nouns():
    f = open("/tmp/words.txt", "w")
    f.write("Ruby\n")
    f.write("Javascript\n")
    f.write("python\n")
    f.write("Perl\n")
    f.close()
    word = hangman.get_secret_word("/tmp/words.txt", selector)
    assert word == "python"

def test_no_init_z():
    f = open("/tmp/words.txt", "w")
    f.write("zruby\n")
    f.write("zjavascript\n")
    f.write("python\n")
    f.write("zperl\n")
    f.close()
    word = hangman.get_secret_word("/tmp/words.txt", selector)
    assert word == "python"
