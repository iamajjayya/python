#collection : Counter ,namedtuple , orderDict ,defaultdict, deque
#counter is a dict subclass for counting hasable object. it is collection where elements are stored as dictionary  keys and thier counts are stored as dictionary values . counts are allowed to be any integer value incuding zero or negative counts
from collections import Counter
a = "abababcacddd"
my_counter =Counter(a)
print(my_counter)
print(my_counter.most_common(3))
print(my_counter.most_common(3)[2])
print(my_counter.most_common(3)[2][1])
print(list(my_counter.elements()))
#Namedtuple is a fcatory function avilable in collection it allows yuo to creates tuple subclasses with named fields. you can access the value in a given named tuple using the dot notation and thr field name,like in obj.attr
from collections import  namedtuple
Point = namedtuple("Ajay","x y")
pt=Point(1,2)
print(pt.x,pt.y)
#orderedDict is a dict subclass that preserves the order in which key values pairs, commonly know an as items are inserted into dictionary.
from collections import  OrderedDict
order_dict =OrderedDict()
order_dict['b']=2
order_dict['c']=3
order_dict['d']=4
order_dict['a']=1
print(order_dict)
#default dic it will return 0,0.0 ,list etc if the key pair does not exit in the dictionary
from collections import defaultdict
d=defaultdict(list)
d['a']=1
d['b']=4
print(d['c'])

#deque is a double ended queue in which elements can be both insterted and deleted from either the left or the right end of the queue
from collections import deque
d =deque()
d.append(2)
d.append(3)
print(d)
d.pop()
print(d)
d.appendleft(3)
print(d)
d.extend([3,4,5])
print(d)
d.clear()
print(d)
d.extend([23,1,2,4,5,5])
print(d)
d.rotate(1)
print(d)
