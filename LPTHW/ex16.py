# get argv feature from sys package
from sys import argv
# unpack argv and assign script and filename to it
script, filename = argv
# priny message ""
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#input prompt "?"
input("?")

print("Opening the file...")
# open file and assign it to target
target = open(filename,"w")

print("Truncating the file. goodbye!")
#turncate target
#target.truncate()

print("Now I'm going to ask you for three lines.")
# assign input to each line
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3 :")

print("I'm going to write these to the file.")
#x = "{}\n{}\n{}\n"
#target.write(x.format(line1,line2,line3))
#write line1 to target
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# close target
target.close()
