#Itertools : Product , Permutation , Combination, accumulate, groupby , and infinite iterators
#itertools is a module in python, it is used to iterate over the data structure that can be steppped over using a for-loop
#product itertool.product() is used to find the cartesian product from the given iterator
from itertools import product
a=[1,2]
b=[4,3]
prod=product(a,b, repeat=2)
print(list(prod))
#permutations
from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print(list(perm))
#Combination
from itertools import  combinations , combinations_with_replacement
a=[1,2,3,4]
comb =combinations(a,2)
print(list(comb))
com_re =combinations_with_replacement(a,2)
print(list(com_re))
#accumulate
from itertools import accumulate
import  operator
a=[1,2,3,2,1]
acc=accumulate(a,func=max)
print(a)
print(list(acc))
#group by operation involves some combination of splitting the object, applying a function , and combining the result
from itertools import groupby

a=[1,2,3,4,5]
grp = groupby(a, key=lambda  x: x<3)
for key ,value in grp:
    print(key,list(value))

colleges =[{"name":"Govt","place":"Bangalore"},
           {"name":"amc","place":"Bangalore"},
           {"name":"loyola","place":"bangalore"}
           ]
grpe =groupby(colleges,key=lambda  x:x["place"])
for key,value in grpe:
    print(key,list(value))
#infinite iterators
from itertools import  count,cycle,repeat
# for i in count(5):
#     print(i)
#     if i==8:
#         break
# a=[1,2,3]
# for i in cycle(a):
#     print(i)
a=[1,2,3]
for i in repeat(3,3):
    print(i)
