##Quiz: Tag Counter
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for index in range(len(items)):
    print('~~~~~~after assign range to index, index is :', index)
    html_str += "<li>" + items[index] + "</li>\n"
    print('~~~~~~~after reassign html_str, html_str is:', html_str)
html_str += "</ul>"

print(html_str)
