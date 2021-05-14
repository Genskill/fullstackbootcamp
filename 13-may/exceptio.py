# exceptio.py

def test1():
    try:
        d = [1,2,3,4,5]
        print (d[100])
    except Exception:
        print ("You've tried to access beyond the last element")

def test2():
    try:
        f = open("/etc/passwdx")
        line = f.readline()
        print (line)
    except (FileNotFoundError,PermissionError) as e:
        print (f"Couldn't open file. Error is '{e}'")
    

test1()

