import unittest

import panagram

def test_positive():
    val = panagram.panagram("the quick brown fox jumps over the lazy dog")
    assert val

def test_negative():
    val = panagram.panagram("the quick brown fox jumps over the slimy dog") # a is missing
    assert val == False

def test_uppercase_positive():
    val = panagram.panagram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    assert val

def test_punctuation():
    val = panagram.panagram("THE,quick BROWN;;;:FOX\\#jumps OVER \n\nThE LAZY    DOG")
    assert val

def test_every_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    assert panagram.panagram(alphabet)
    for i in alphabet:
        test_case = alphabet.replace(i,"")
        assert panagram.panagram(test_case) == False
            
