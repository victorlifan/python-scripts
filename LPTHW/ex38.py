ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list, let's fix that.")
# split(ten_things by '') then assign to variable "stuff"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night","Song","Friebee",
                "Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    # pop (more_stuff) last element, assign it to variable "next_one"
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    # append( next_one) to stuff
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
# pop (stuff) last element and print out
print(stuff.pop())
# join (stuff) with space
print(''.join(stuff))#what? cool!
# join element 3:5 in stuff with #
print('#'.join(stuff[3:5]))#super stellar!
