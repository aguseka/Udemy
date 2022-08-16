import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Peter"},
          {"firstName": "Jessy", "lastName": "Peter"}]}
d["employees"].append(dict(firstName = "Albert", lastName = "Einstein"))
d["employees"].append(dict(firstName = "Eka", lastName = "Maharta" ))
d["employees"].append(dict(namaDepan = "Satria", namaBelakang = "Dharma" ))

with open("employee.json", "w") as jsonfile:
    json.dump(d,jsonfile, indent= 4)