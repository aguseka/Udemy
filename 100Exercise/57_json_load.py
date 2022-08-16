import json
from pprint import pprint

with open("employee.json", "r") as jsonfile:
    d = json.loads(jsonfile.read())

pprint(d)