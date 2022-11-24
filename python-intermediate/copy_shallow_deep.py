org=5
cpy=org
cpy=6
print(cpy)
print(org)

# shallow copy :one level deep , only references of nested child objects
#deep copy : full independent copy
import copy
org=[1,2,3,45,5]
cpy=copy.deepcopy(org)
# cpy=list(org)

cpy[0]=6
print(cpy)
print(org)
