#dict creation
person_details = {
    "name" : "Aswini",
    "age"  : 24,
    "company_name" : "Letitbexai"
    }
print(person_details)

#keys must be unique otherwise it may be replace with the latest value
person_details = {
    "name" : "Aswini",
    "name" : "aswini padileti",
    "age"  : 24,
    "company_name" : "Letitbexai"
    }
print(person_details)

#dict methods #get
student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.get("name"))
print(student.get("age"))

#keys returns all the keys that are present in the dictionary 
student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.keys())

#values returns all the values that are present in the dict
student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.values())

#items returns both the keys and values together as tuples
student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.items())

#update updates a new item or updates an existing item
student = {
    "name":"Aswini"
    }
student.update({"age":22})
print(student)

#pop removes a specified key  and returns a value
student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.pop("age"))
print(student)

student = {
    "name" : "aswini",
    "age"  : 24
    }
print(student.clear())
print(student)

#nested dictinaries 
students = {
    101: {
        "name": "Aswini",
        "age": 22
    },
    102: {
        "name": "Rahul",
        "age": 23
    }
}
print(students)

#iterating means accessing or processing dictinoary elements through keys
data = {
    "name" : "aswini",
    "age"  : 24,
    "company" : "letitbexai"
}

for key in data:
    print(key)
#iteration through values
data = {
    "name" : "aswini",
    "age"  : 24,
    "company" : "letitbexai"
}

for value in data:
    print(value)
#iteration through key pair values
data = {
    "name" : "aswini",
    "age"  : 24,
    "company" : "letitbexai"
}

for key , value in data.items():
    print(key, ":" ,value)