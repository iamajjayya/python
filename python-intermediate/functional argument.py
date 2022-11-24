def print_name(name): #parameter
    print(name)

print_name("ajay")#argument

#keyward argument
def keyword_argu(a,b,c):
    print(a,b,c)

keyword_argu(c=1,b=6,a=5)

#variable length argument

def args_kawrgs(a,b,*args,**kwargs):
    print(a,b)
    for args in args:
        print(args)
    for kargus in kwargs:
        print(kargus,kwargs[kargus])
args_kawrgs(1,2,3,4,5,6,7,eight=8,nine=9,ten=10)


#unpacked list / tuple

def un_list(a,b):
    print(a,b)
my_list =[1,2]
un_list(*my_list)

def un_dick(a,b):
    print(a,b)
my_dict ={'a':1,'b':2}
un_dick(**my_dict)

#global variable

# def global_variable():
#     global nu
#     nu=3
#     print(nu)
# global_variable()
# nu=5
# print(nu)

