import json
from pprint import pprint

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "Kartika", lasName = "Maharta"))
    d["owners"].append(dict(firstName="Eka", lasName="Aditya"))
    file.seek(0)
    json.dump(d, file, indent = 4, sort_keys=True)
    file.truncate()