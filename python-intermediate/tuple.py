#tuple ordered, imutable allows duplicate elements

mytuble = ("tuple",)
print(type(mytuble))

#accesing elements
mytuble_elements = tuple(["python",1,True])
print(mytuble_elements)
item =mytuble_elements[1:]
print(item)

#tuples are imutable
#mytuble_elements[0]="java"
#print(mytuble_elements)

import  sys
my_list =[10,"ajay","python"]
my_tuple=(10,"ajay","python")
print("List and Tuple Difference and why should we use Tuble")
print("1. Size")
print(sys.getsizeof(my_list),"bytes")

print(sys.getsizeof(my_tuple),"bytes")

import timeit
print("2. Time/Speed")
print(timeit.timeit(stmt='[0,2,3,4]',number=100000))

print(timeit.timeit(stmt='(0,2,3,4)',number=100000))

#dont use tuple when we want to change elements in future