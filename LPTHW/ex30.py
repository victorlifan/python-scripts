people = 2
cars = 1
trucks = 1

# add "if" statement, add arguement cars > people
if cars > people:
    # print meg if the arguement is true
    print("We should take the cars.")
# "elif" statement
elif cars < people:
    # print meg if arguement is true
    print("We should not take the cars.")
# "else" statement
else:
    # print msg if "elif" is not true
    print("We can't decide.")
# add "if" statement, arguement "truck > cars"
if trucks > cars:
    # print msg if arguement is true
    print("That's too many trucks.")
# add "elif" statement, arguement "trucks < cars"
elif trucks < cars:
    # print msg if arguement is true
    print("Maybe we could take to trucks.")
# add "else" statement
else:
    # print msg if "elif" is not true
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay gome then.")
