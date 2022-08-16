from pprint import pprint

e = dict(a = list(range(1,11)), b = list(range(11,21)), c = list(range(21,31)),)

for key,value in e.items():
    print(key, "Has value of", value)
print("\n")