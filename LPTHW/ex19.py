# define function named "cheese_and_crackers" with args "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print codes in the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enough for a party!")
    print("Get a blanket.\n")

# run the function by giving numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# assign numbers to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# run the function by giving variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# run the function by giving maths
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# run the function by combing math and number together
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
