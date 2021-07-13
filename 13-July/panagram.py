def panagram(s):
    s = s.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True
