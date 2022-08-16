import glob

file_list = glob.glob("huruf/*.txt")
mylist = []


for file in file_list:
    with open(file, "r") as f:
        mylist.append(f.read().strip("\n"))

print(mylist)
