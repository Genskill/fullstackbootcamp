def ndigits(n):
    r = len(str(abs(n)))
    return r

def nwords(s):
    words = s.split(" ")
    return len(words)

def nsentences(s):
    return s.count(".") + s.count("!") + s.count("?")

def largest(a, b, c):
    """This is a function to return the largest of 3 integers"""
    if a > b:
        if a > c:  # a is > b an c
            return a
        else:
            return c # c is > a and b
    else:
        if b > c: 
            return b # b is > a and c
        else:
            return c # c is > a and b

def category(n):
    if n < 10:
        return "sub junior"
    elif n < 15:
        return "junior"
    elif n < 20:
        return "cadet"
    elif n < 30:
        return "senior"
    else:
        return "veteran"
    
def verify_password():
    secret = "topsecret"
    got = input("Enter password ")

    while got != secret:
        got = input("Enter password ")

    print ("Success")
    return True    

def average(l):
    """Returns the average of the numbers in list l"""
    count = len(l)
    total = 0
    for i in l:
        print (f"Adding {i}")
        total = total + i
    return total/count
 
def panagram(s):
    """Returns True if s is a panagram. False otherwise"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in s:
            print (f"{i} is missing")
            return False
    return True

def dumpfile(fname):
    f = open(fname)
    for i in f:
        print (i)
    f.close()
