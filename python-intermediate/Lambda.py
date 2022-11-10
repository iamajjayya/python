#lamda argument : expression
one_argument =lambda x: x+10
print(one_argument(5))
two_argument =lambda  x,y:x*y
print(two_argument(3,5))
#sorting
sort2d=[(1,3,1),(3,4,4),(5,2,3),(1,9,8)]
print_sort =sorted(sort2d,key= lambda x: x[2])
print(sort2d)
print(print_sort)

sort2d=[(1,3,1),(3,4,4),(5,2,3),(1,9,8)]
print_sort =sorted(sort2d,key= lambda x: x[0]+x[1])
print(sort2d)
print(print_sort)

#map(function) map(function ,seq)
a=[1,2,3,4]
b=map(lambda  x: x+2, a)
print(list(b))
#filter function filter(function, seq)
a=[1,2,3,4]
b=filter(lambda  x: x%2==0, a)
print(list(b))

c=[ x for x in a if x%2==0]
print(c)

#reduce function
from functools import  reduce
a=[1,2,3,4]
reduce_fun =reduce(lambda x,y: x*y ,a)
print(reduce_fun)
