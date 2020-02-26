##q1
start_num = 1#provide some start number
end_num = 4#provide some end number that you stop when you hit
count_by = 1#provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)

##q2
start_num = 1#provide some start number
end_num = 4#provide some end number that you stop when you hit
count_by = 1#provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
if start_num <= end_num:
    while break_num < end_num:
        break_num += count_by
else:
    break_num = 'Oops! Looks like your start value is greater than the end value. Please try again.'
print(break_num)

##q3
limit = 40

# write your while loop here
number = 1
while number**2 < limit:
    number += 1
nearest_square = (number -1)**2

print(nearest_square)
