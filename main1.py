#load is used to read the data and it converts into the python object
import json
with open("student.json", "r")as file:
    data = json.load(file)
    print(data)
    print(type(data))
#Loads reading json is used to convert json formatted string into python object
import json
data = '{"name": "Aswini", "age": 24}'
result = json.loads(data)
print(result)
print(type(result))

#json dump is used for writing json into a python file it converts json object into a file
import json
data = {
    "name": "Aswini",
    "age": 22
}
with open("data.json", "w") as file:
    json.dump(data, file)

#dumps converts python object into json string
import json
data = {
    "name": "Aswini",
    "age": 22
}
result = json.dumps(data)
print(result)
print(type(result))

#sort_key parameters arranges the dictioanry keys in a alphaabetical order
import json
student = {
    "name" : "Aswini",
    "age" : 24
}
print(json.dumps(student, indent=4, sort_keys= True))
