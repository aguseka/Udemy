import string

letters_1 = string.ascii_lowercase[0::3]
letters_2 = string.ascii_lowercase[1::3]
letters_3 = string.ascii_lowercase[2::3]


with open("words5.txt", "x") as file:
    for x, y , z in zip(letters_1, letters_2, letters_3):
        file.write(x+y+z + "\n")