import string, os
if not os.path.exists("huruf"):
    os.makedirs("huruf")
letter = string.ascii_lowercase
for alphabet in letter:
    with open( "huruf/" + alphabet + ".txt", "w") as file:
        file.write( alphabet + "\n")