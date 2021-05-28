import random # Standard library module to select words randomly

# These variables are used to return statuses when we check words. The
# numbers have no special meaning. It's easier to understand what
# something like
#        if check_guess(...) == REPEAT:
# means rather than 
#        if check_guess(...) == 100
# These are what we call "symbolic constants"

REPEAT = 100
CORRECT = 200
WRONG = 300
DEAD = 400
SUCCESS = 500

def get_word(fname):
    """This function will get a word from the file fname that satisfies
    the following criteria
    1. Aleast 5 letters
    2. First letter shouldn't be capital  (no proper nouns)
    3. No punctuation

>>> get_word("/usr/share/dict/words")
'mitigating'
>>> get_word("/usr/share/dict/words")
'soiling'
>>> get_word("/usr/share/dict/words")
'slacking'
>>> get_word("/usr/share/dict/words")
'inamorata'
    """
    good_words = [] # List of good words we can use
    f = open(fname)
    for i in f:
        i = i.strip() # Remove the \n (newline) at the end of the word

        if len(i) < 5: # Criterion 1. Atleast 5 letters
            continue # If it's less than 5 letters, skip and go to the next word
        if i.istitle(): #Criterion 2. First letter shouldn't be capital. 
            continue # If it is capital, skip and go to the next word
        if not i.isalpha(): # Contains numbers or punctuations
            continue # If it's not alphabetical, skip and go to the next word

        good_words.append(i) # add it to the list of good words

    return random.choice(good_words) # Selects a random word out of
                                     # the list of good words and
                                     # returns it.

def mask_word(word, letters_to_show):
    """
    Will take a word and a list of letters to be shown (correct guesses
    so far) and return a string that shows the word with _ for letters
    to be masked.
    
>>> mask_word("elephant", ["p", "h", "t"])
'___ph__t'
>>> mask_word("elephant", ["e"])
'e_e_____'
    """
    op = [] # Empty string to hold characters to display
    for i in word: # For each input letter
        if i in letters_to_show: # If i is a letter than needs to be shown
            op.append(i)         #     Add it to the list of output letters
        else:
            op.append("_")       #     Add _ to the list of output letters
    return "".join(op) 
            
    
def create_status(word, guesses, turns_left): 
    guesses = " ".join(guesses)
    word = mask_word(word, guesses)
    return f"""Word : {word}
Guesses : {guesses}
Turns left : {turns_left}"""

def check_guess(word, letter, guesses, turns_left):
    """
    Checks
    """
    all_guessed = True
    t = guesses + [letter] # NEed to consider the new guess as well.
    for i in word:
        if i not in t:
            all_guessed = False
    if all_guessed:
        return SUCCESS

    if letter in guesses:
        return REPEAT
    elif letter in word:
        return CORRECT
    else:
        if turns_left == 1:
            return DEAD
        else:
            return WRONG

def main():
    turns_left = 10
    guesses = []
    word = get_word("/usr/share/dict/words")
    # print (word) # Uncomment this if you want to see the word
    while True:
        status = create_status(word, guesses, turns_left)
        print (status)
        guess = input("Enter input and hit enter ")

        r = check_guess(word, guess, guesses, turns_left) # Check the new guess

        if r == CORRECT: # If it's a correct guess
            guesses.append(guess) # Add the guess to the list of guesses
        elif r == REPEAT: # Else if it's a repeated guess
            print (f"You've already guessed '{guess}'") # Don't do anything
        elif r == WRONG: # Else if it's a wrong guess
            turns_left -= 1 # Reduce number of turns (bad guess)
            guesses.append(guess) # Add guess to list of guesses
        elif r == DEAD: # Failed. Print the word and break out the loop.
            print (f"Sorry! You've run out of turns. The word was '{word}'")
            break
        elif r == SUCCESS: # Succeeded. Print the word and break out the loop.
            print (f"Congratulations! You got it. The word was '{word}'")
            break


main()
