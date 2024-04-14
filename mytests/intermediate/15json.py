# Serialization, convert py dict to json
# import json 

# person = {"name": "Peter", "age": 28, "city": "London", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4, sort_keys=True) # Indent - indentation, sort keys optional (dimp s for string)
# # print(personJSON)

# # Save to file
# # with open('example.json', 'w') as f:
# #     json.dump(person, f, indent=4) # dump to save to file

# # Deserialization to py
# person = json.loads(personJSON)
# print(person)
# # and from file:
# with open('example.json', 'r') as f:
#     person = json.load(f)
#     print(person)

# Custom serialization
# import json 
# class User:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
# user = User('Max', 54)

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True} # optional: o.__class__.__name__: True 
#     else:
#         raise TypeError('Object is not JSON serializable')

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

# Another serialization
# import json 
# class User:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
# user = User('Max', 54)

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True} # optional: o.__class__.__name__: True 
#     else:
#         raise TypeError('Object is not JSON serializable')
    
# from json import JSONEncoder 
# class UserEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o, User):
#             return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#         return JSONEncoder.default(self, o)

# userJSON = json.dumps(user, cls=UserEncoder)
# print(userJSON)


# Another serialization
import json 
class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

user = User('Max', 54)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} # optional: o.__class__.__name__: True 
    else:
        raise TypeError('Object is not JSON serializable')
    
from json import JSONEncoder 
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
print(userJSON)


# Decode to call dict object values
def decode_user(dct):
    if User.__name__ in dct: # check ih key is dictionary
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user)
print(type(user))
print(user.name)