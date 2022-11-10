# Strings :orderd ,imutable ,text Representation
my_string='hello world'
print(my_string)
my_string="'hello world"
print(my_string)
my_string="""hello 
world"""
print(my_string)
#accesing character
my_string ="hello"
print(my_string[0])
#imutable
my_string="hello"
# my_string[0]="a"
print(my_string)
#slicing
my_string="hello"
print(my_string[::3])
#concatinating
greeting ="good morning"
name="ajay"
sentence =greeting+"  "+name
print(sentence)
#iteration
strings ="hello"
for greeting in strings:
    print(greeting)
#substring
if "he" in strings:
    print("yes")
else:
    print("No")
#Stripe
my_string ="  hello  "
my_string =my_string.strip()
print(my_string)

#uppercase
strings ="hello India"
print(strings.upper())
# lowercase
strings ="hello India"
print(strings.lower())
#startswith
strings ="hello India"
print(strings.startswith("he"))
#endswith
strings ="hello India"
print(strings.endswith("ia"))
#replace
strings ="hello India"
print(strings.replace("hello","Namaskara"))
#string ro list
asking ="what,are,u,doing"
asking_list=asking.split(",")
print(asking_list)

new_string =' '.join(asking_list)
print(new_string)
#list to string
from  timeit import  default_timer as timer

my_list =['a'] * 100
print(my_list)
start =timer()
my_string =''
for i in my_list:
    my_string +=i
print(my_string)
stop =timer()
print(stop-start)
#or
start =timer()
my_string = ''.join(my_list)
print(my_string)
stop =timer()
print(stop-start)
#string format %, format() ,f-string
#%
var =3.17199
strings =" tha var is %.3f" %var
print(strings)
#format
string1 ="hello"
string2 ="ajay"
my_string ="string1 {} and string2 {}".format(string1,string2)
print(my_string)
#f string
string1 ="hello"
string2 =122
my_string =f"string1 {string1} and string2 {string2+2}"
print(my_string)
print("ajjayya")


