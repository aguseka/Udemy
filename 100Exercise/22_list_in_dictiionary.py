from pprint import pprint

e = dict(a = list(range(1,11)),
b = list(range(11,21)),
c = list(range(21,31)),)

print ("This is my version \n")
for key,value in e.items():
    print(key,value)
print("\n")

print ("This is the instructor version \n" )
pprint(e)