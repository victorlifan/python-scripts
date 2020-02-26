num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_num = []
for num_lists in num_list:
    if num_lists%2 != 0:
        odd_num.append(num_lists)
result = sum(odd_num[:5])
print(result)
