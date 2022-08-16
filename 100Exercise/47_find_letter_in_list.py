import glob

file_list = glob.glob("huruf/*.txt")
mylist = []
check = "python"

for file in file_list:
    with open(file, "r") as f:
        l = f.read().strip("\n")
    print(l)
    if l in check:
            mylist.append(l)

print(mylist)
