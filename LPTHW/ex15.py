# import from mudual sys
from sys import argv
# assign script and filename to argv
script, filename = argv
# open file i just assigned to argv then assign txt to it
txt = open(filename)
# print message ""
print(f"Here's your file {filename}:")
# give command to read txt then print out
print(txt.read())
txt.close()

# print message ""
print("Type the filename again:")
# assign input">"" to file_again
file_again = input("> ")
# opne file_again and assign it to txt_again
txt_again = open(file_again)
# read txt_again then print out
print(txt_again.read())
txt_again.close()
