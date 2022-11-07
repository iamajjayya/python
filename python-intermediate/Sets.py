#Sets : Unordered,Mutable, No duplicates

myset = {1,2,3,1,4}
print(myset)

#Another Way
mysetString =set("Hello")
print(mysetString)

#tuple
mysettuple ={}
print(type(mysettuple))
#set
mysetex =set()
print(type(mysetex))

# Mutable
myset_mutable =set()
myset_mutable.add(1)
myset_mutable.add(2)
myset_mutable.add(3)
myset_mutable.add(4)

print(myset_mutable)

#forloop
for a in myset_mutable:
    print(a)
# unions , intersection

odd ={1,3,5,7,9}
evens ={0,2,4,6,8}
primes={2,3,5,7}

u=odd.union(evens)
print(u)
i=odd.intersection(primes)
print(i)

#Difference
# 1
setA ={1,2,3,4,5}
setB ={1,2,3,6,7}
differnce = setA.difference(setB)
print(differnce)
# 2
setA ={1,2,3,4,5}
setB ={1,2,3,6,7}
differnce = setB.difference(setA)
print(differnce)
#3
setA ={1,2,3,4,5}
setB ={1,2,3,6,7}
differnce = setA.symmetric_difference(setB)
print(differnce)
# 4
setA ={1,2,3,4,5}
setB ={1,2,3,6,7}
setB.symmetric_difference_update(setA)
print(setB)
#Subset ,SuperSEt
setA={1,2,3,4,5,6,7}
setB={1,2,3}
print(setA.issubset(setB))
# 2
etA={1,2,3,4,5,6,7}
setB={1,2,3}
print(setA.issuperset(setB))
# 3
setA={4,7}
setB={1,2,3}
print(setA.isdisjoint(setB))
#copy
setA={1,2,3}
setB=set(setA)
setA.add(4)
print(setB)
print(setA)
#frozenset
a=frozenset([1,2,3,4,5])

print(a)
