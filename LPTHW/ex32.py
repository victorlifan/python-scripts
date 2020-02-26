# make a list "the_count" that has elements [1,2,3,4]
the_count = [1,2,3]
# make a list "fruits" that has elements [apple, oranges ,pears, apricots]
fruits = ['apples','oranges','pears','apricots']
# make list of "change" that has elements [1, pennies, 2, dimes, 3, quarters]
change = [1,'pennies',2,'dimes',3,'quarters']

#assign all the elements in "the_count" to variable "number"
for number in the_count:
    # print out msg
    print(f"This is count {number}")

# assign all the elements in "fruits" to variable "fruit"
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# assign all the elements in "change" to variable "i"
for i in change:
    print(f"I got {i}")

# make a list elements has no elements in
elements = []

# then use the range function to do 0 to 5 counts, assign 0~5 elements to variable "i"
for i in range(0,6):
    # then print out msg
    print(f"Adding {i} to the list.")
    # append is a function that lists understand, append variable "i" to list "elements"
    elements.append(i)
# assign all the elements in "elements" to variable "o" then print
for o in elements:
    print(f"Element was :{o}")
