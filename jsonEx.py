# Run in Python37
import json
from json import JSONEncoder

'''
- Learn how to convert Python objects to JSON data
'''
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
personJSON = json.dumps(person, indent=2, sort_keys=True, )

# print(person_json)

# Create a JSON data file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=2)
    
# Convert it back to Python dict
personDict = json.loads(personJSON)
# print(personDict)

# Open as the read mode
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
    

class User:
    def __init__(self, name,age):
        self.name = name
        self.age = age

user = User('Max',27)

# userJSON = json.dumps(user) 
''' 
At this time, u gonna facing the following error message: TypeError: Object of type User is not JSON serializable
=> Write a custom encoding function
'''
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} # Class name as a key, 
    else: 
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON = json.dumps(user, cls=UserEncoder) # or an alternative one: UserEncoder().encode(user)
# print(userJSON)

# Convert the user JSON to dict
user = json.loads(userJSON)
print(user) # we have a dict here
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
    

            
        
