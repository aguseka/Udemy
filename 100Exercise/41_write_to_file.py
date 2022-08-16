#open file using context manager


import string
with open("words3.txt", 'x') as file:
    for letter in string.ascii_lowercase:
        file.write(letter +"\n")