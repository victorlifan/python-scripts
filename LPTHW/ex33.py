# assign value 0 to variable i
i = 0
# assign list to variable "numbers"
numbers = []
# while loop. while i < 6 do:
while i < 6:
#print msg
    print(f"At the top i is {i}")
# append "i" to list "numbers"
    numbers.append(i)
# assign new value "i + 1" to variable "i"
    i = i + 1
# print msg
    print("Numbers now:", numbers)
# print msgnew new "i" value
    print(f"At the bottom i is {i}")


print("The numbers:")
# assign all the elements in "numbers" to variable "num"
for num in numbers:
    #print num
    print(num)
