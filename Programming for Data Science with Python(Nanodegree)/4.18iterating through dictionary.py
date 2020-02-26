# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.
##task 1 method 1
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit in fruits:
    result += basket_items.get(fruit,0)
print(result)

## task 1 method 2
for object, count in basket_items.item():
    if object in fruits:
        result += count
print(result)

## task 3
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items:
#if the key is in the list of fruits, add to fruit_count.
    if object in fruits:
        fruit_count += count
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)
