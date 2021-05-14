# countdown.py

def countdown(n):
    upper_limit = n
    while upper_limit != 0:
        print (upper_limit)
        # n = n - 1
        upper_limit -= 1

def truncate(l):
    # while len(l) != 0: # This is non idomatic usage
    while l: # Pythonic way
        t = l.pop()
        print (len(l), t)

# truncate(["python", "perl", "ruby", "php", "javascript"])

countdown(10)
        
