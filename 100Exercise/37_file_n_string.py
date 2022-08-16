def readingwords(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng = strng.replace("," , " ")
        strng_list = strng.split(" ")
        return len(strng_list)

print (readingwords("words2.txt"))


''' Alternate solution'''

import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)


print(count_words_re("words2.txt"))