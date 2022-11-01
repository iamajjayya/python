#Lists  ordered,mutable and allows dupicate elements

#strings
mylist_strings = ["12","10","python"]
print(mylist_strings)

#numbers
mylist_numbers=[20,-12]
print(mylist_numbers)

#boolean
mylist_boolean =[True,False]
print(mylist_boolean)

#example and indexing
mylist_index = ["apple","bannan","cheery","dog","orange","zebra"]
print(mylist_index)

item =mylist_index[2:-2]
print(item)

#for loop

#1
for i in mylist_index:
    print(i)
#2
print("---Indexing in for loop ---")
for i in mylist_index[4:]:
    print(i)

#emptylist

mylist_empty = list()
print(mylist_empty)

#if elese
mylist_if =["ajay","jeevan","hema"]
if "ajay" in mylist_if:
    print("Yes")
else:
    print("No")

mylist_if = ["ajay", "jeevan", "hema"]
if "gv" in mylist_if:
        print("Yes")
else:
        print("No")

#methods
mylist_method = [1,2,5,4,2,6,9]
print(mylist_method)
print("append",mylist_method.append(10))
print(mylist_method)
print("pop",mylist_method.pop())
print(mylist_method)
print("insert",mylist_method.insert(2,3))
print(mylist_method)
print("remove",mylist_method.remove(1))
print(mylist_method)
print("reverse",mylist_method.reverse())
print(mylist_method)
print("sort",mylist_method.sort())
print(mylist_method)

#operators

mylist_operators =[1] * 6
print(mylist_operators)

mylist_old = ["a","b"]
mylist_new=["c","d"]
print(mylist_old+mylist_new)

#slicing

mylist_slicing = [1,2,3,4,5,6,7,8,9]
slicing = mylist_slicing[2:4]
print(slicing)

#copy list

mylist_newlist =[1,2]
mylist_copy =mylist_newlist.copy()
print(mylist_newlist.append(3))
print(mylist_copy)

ab = [2,3,4,5]
ba = [i*i for i in ab]
print(ba)