# call sys module
import sys
# assign script, input_encoding, error to argv and import argv
script, input_encoding, error = sys.argv

# call function "main" assign arguements into function
def main(language_file, encoding, errors):
    # read one line of languages_file (which is languages.txt) and assign it to line
    line = language_file.readline()
    # "if" statement, if line doesn't exist, it ends, if exist then run following:
    if line:
        #  run function "print_line"
        print_line(line, encoding, errors)
        # return to "main" function
        return main(language_file, encoding, errors)

# call function "print_line" and assign arguements
def print_line(line, encoding, errors):
    # assgin line.strip() to next_lang
    next_lang = line.strip()
    # assign (line.strip()).encode(utf-8, errors=errors) to raw_bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # inverse, assign cooked_string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # print out raw_bytes and cooked_string
    print(raw_bytes, "<===>", cooked_string)

# open languages.txt and use utf-8 to encode then assign it to languages
languages = open("languages.txt", encoding="utf-8")
# run function "main"
main(languages, input_encoding, error)
