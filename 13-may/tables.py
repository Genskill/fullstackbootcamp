# tables.py

def loop_list():
    for i in [1, 2, 3, 4]:
        print (i)

def loop_string():
    for i in "noufal":
        print (i)
  
def loop_dict():
    d = {"name" : "Noufal", "place" : "Calicut"}
    for i in d:
        print (i)
    print ("------")
    for i in d.values():
        print (i)
    print ("------")
    for k,v in d.items(): # Idiomatic
        print (f"Key is {k} and value is {v}")

def loop_int():
    # This will not work. This is an error since numbers are not iterable
    for i in 12345:
        print (i)

def loop_range():
    for i in range(1, 20, 2):
        print (i)

def tables(of, upto):
    for i in range(1, upto+1):
        print (f"{of} x {i} = {of*i}")

tables(5, 15)


