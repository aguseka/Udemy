import string
with open("words4.txt", 'x') as file:
    for i,j in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(i+j +"\n")