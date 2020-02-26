# import modual ex25
import ex25
# assign string to variable "sentence"
sentence = "All good things come to those who wait."
# enter "sentence" as the arguement into function "break_words", return an array of the words and assign to "words"
words = ex25.break_words(sentence)
# show the value of "words"
words
# call function "sorted_words", enter words array as arguement, it returns sorted(words) value and assign to sort_words function
sorted_words = ex25.sort_words(words)
# show the value "sorted_words"
sorted_words
# call funtcion "print_first_word" in modual ex25. enter words array as arguement. first word is printed
ex25.print_first_word(words)
# same, last word is printed
ex25.print_last_word(words)
#show the value of words, the first and last word will be missing, because the previous two function called removed first and last elements
words
#call function "print_first_word" again, assign valuesorted_words array as an arguement this time, print the first word
ex25.print_first_word(sorted_words)
#same, print the last word
ex25.print_last_word(sorted_words)
#show sorted words value without first and last elements
sorted_words
# call function"sort_sentence" in modual ex25, enter "sentence" as arguement, assign the return to to sorted_words
sorted_words = ex25.sort_sentence(sentence)
# show the value of sorted_words
sorted_words
#call function "print_first_and_last", enter "sentence" as arguement, first and last is printed
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
