def break_words(stuff):
    print("<<<function break_words:", break_words)
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
    print(">>>exit function break_words")

def sort_words(words):
    print("<<<funtcion sort_words:", sort_words)
    """Sorts the words."""
    return sorted(words)
    print(">>>>exit function sort_words")

def print_first_word(words):
    print("<<<<function print_first_word",print_first_word)
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    print(">>>>exit function print_first_word")

def print_last_word(words):
    print("<<<<<<function print_last_word:", print_last_word)
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    print(">>>>exit function print_last_word")
def sort_sentence(sentence):
    print("<<<function sort_sentence:", sort_sentence)
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    print(">>>exit function sort_sentence")
def print_first_and_last(sentence):
    print("<<<<<function print_first_and_last,": print_first_and_last)
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print("~~~~~call function print_first_word:", print_first_word)
    print_first_word(words)
    print("~~~~~~~~~end call print_first_word")
    print("~~~~call funtcion print_last_word:", print_last_word)
    print_last_word(words)
    print("~~~~~~~end call print_last_word")
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
