print("Let's parctice everything.")
print('You\'d need to know\' about escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovly world
with logic so frimly planted
cannot discern \nthe needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\twhere there is none.
"""
x = "-"
print(x*14)
print(poem)
print(x*14)


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
# call function "secret_formula", add arguement "strated"
def secret_formula(started):
    # equations
    jelly_beans = started *500
    jars = jelly_beans / 1000
    crates = jars / 1000
    # return values of jelly_beans, jars, crates
    return jelly_beans, jars, crates

# assign value to variable "start_point"
start_point = 10000
# run function "secret_formula" with value 10000, assign return value to variable bean etc.
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of : {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
# assign value 1000 to variable "start_point"
start_point = start_point / 10

print("We can also do that this way:")
# assign function secret_formula to a valable"formula"
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format starting
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
