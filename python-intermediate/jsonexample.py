#
# import  json
# person ={ "Name" :"Ajjayya" ,"age":20 , "graduation":True , "Skills":["Python","Java","React"] }
# personjson = json.dumps(person,indent=4, sort_keys=True)
# print(personjson)
#
# # with open('person.json', 'w') as file:
# #     json.dump(person, file, indent=4)
#
# #json to dictonary
#
# person =json.loads(personjson)
# print(person)
#

import json

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user = User('Ajjayya',20 )
def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError(" user is not json serialization")
userJson =json.dumps(user , default=encode_user)
print(userJson)
def decoder_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],age=dct['age'])
    return  dct


user =json.loads(userJson, object_hook=decoder_user)
print(user.name)




