# call function "add" with arguements a,b
def add(a,b):
# print meg "ADDING a + b"
    print(f"ADDING {a} + {b}")
# return the result to age
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDEING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")
# run "add" function with value 30, 5
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the sxtra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight,divide(iq, 2))))
#what_1 = divide(iq, 2)
#what_2 = multiply(weight, what_1)
#what_3 = subtract(height, what_2)
#what_4 = add(age, what_3)
#print(what_4)
print("That become:", what, "Can you do it by hand?")
