import random
# a=random.uniform(1,10)
# print(a)


#it will pick any one element
# mylist =list("ABCDEF")
# a=random.choice(mylist)
# print

#sample print any group element ex= random.sample(mylist,numberofelementtobeprint) and element will not print twice
# mylist =list("ABCDEF")
# a=random.sample(mylist,4)
# print(a)

#sample print any group element and it will print repeat
# mylist =list("ABCDEF")
# a=random.choices(mylist,k=4)
# print(a)


#element will be shuffle
# mylist =list("ABCDEF")
# random.shuffle(mylist)
# print(mylist)

#seed

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(1)
# print(random.random())
# print(random.randint(1,10))

import  secrets

# a=secrets.randbelow(10)
# print(a)

# a=secrets.randbits(4)
# print(a)

# mylist = list("ABCDEFGH")
# a=secrets.choice(mylist)
# print(a)
import  numpy
# a=numpy.random.randint(0,10,(3,5))
# b=numpy.random.randint(0,10,(3,5))
#
# print(a)
# print(b)
# print(a+b)

arr = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
numpy.random.shuffle(arr)
print(arr)