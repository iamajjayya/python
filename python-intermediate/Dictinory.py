#Dictionary : Key pairs, Unordered,Mutable
mydict = {"name":"ajay","age":20,"place":"Bangalore"}
print(mydict)
#Alternative
mydict1 = dict(name="ajay", age=20,city="bangalore")
print(mydict1)
keyvalue = mydict1["name"]
print(keyvalue)
#mutable
mydict1["email"]="ajay@gmail.com"
print(mydict1)
mydict1["age"]=19
print(mydict1)
#del
del mydict1["name"]
print(mydict1)
mydict1.pop("age")
print(mydict1)
#popitem removes last element
mydict1.popitem()
print(mydict1)


mydict1["name"]="ajay"
print(mydict1)
#if statemnt
if "name" in mydict1:
    print(mydict1["name"])

#tre and except

try:
    print(mydict1["city"])
except:
    print("City is not there in a Dictionary")

try:
    print(mydict1["citY"])
except:
    print("City is not there in a Dictionary"," , Look Y,Python is case sensitive")
#for loop
#keys
for key in mydict1:
    print(key)
#another way
for key in mydict1.keys():
    print(key)

#value
for values in mydict1.values():
    print(values)
#key and values
for key,values in mydict1.items():
    print(key,values)
#copy
mydict_new ={"name":"ajay","age":20}
print(mydict_new)
mydict_old = mydict_new
print(mydict_old)
#mutable
mydict_old["name"]="Ajay"
print(mydict_old)
print(mydict_new)

#update
mydic1 ={"place":"Bangalore"}
mydic2 = {"Age":20}
mydic1.update(mydic2)
print(mydict1)

#numbers keys
my_keys={1:2,3:4}
print(my_keys)

values = my_keys[1]
print(values)

#tuple also use as key
my_tuple = ("name")
my_dict ={my_tuple:"ajay"}
print(my_dict)

#But in list is not possible


