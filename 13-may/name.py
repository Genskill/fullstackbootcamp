# name.py

def main():
    name = input("Enter your name ")
    age = input("Enter your age ")
    age = int(age)

    if age < 18:
        print ("You can't vote yet!")
        print ("Why are you here?")
        print ("Did you get your parents permission?")
    elif age < 55:
        print ("Not retired yet. Good.")
    else:
        print ("Glad to see you healthy and fit")

    print (f"Hi {name}. I see you are {age} years old")

main()
