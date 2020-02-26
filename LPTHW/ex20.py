# call sys modual import argv
from sys import argv
# assign ex20.py & test.txt file to argv
script, input_file = argv
# call function "print_all" add arguement "f"
def print_all(f):
# read "f" then print it out
    print(f.read())
# call function "rewind" add argument "f"
def rewind(f):
# move the read location to the beginging of the file
    f.seek(0)
# call function "print_a_line" add arguement (line_count, f)
def print_a_line(line_count, f):
# read one line of the text in "f", print line_count and one line of "f"
    print(line_count, f.readline())
# open terst.txt then assign it ot current_file
current_file = open(input_file)
# print message ""
print("First let's print the whole file:\n")
# run function "print_all": open test.txt read then print
print_all(current_file)
# print msg""
print("Now let's rewind, kind of like a tape.")
# run function "rewind": open test.txt read it from the begining
rewind(current_file)
# print meg ""
print("Let's print three lines:")
# assign first line to current_line
current_line = 1
# run function"print_a_line" which print first line of test.txt
print_a_line(current_line, current_file)
# assign 2nd line to current_line
current_line = current_line + 1
# run function print_a_line which read 2nd line of test.txt
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
