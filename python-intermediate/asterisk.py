# result = 2**4
# print(result)
numbers =[1,2,3,4,5,6,7,8,9]

*beg , last =numbers
print(beg)
print(last)

def fun(a,b,*args,**kargs):
    print(a,b)
    for ar in args:
        print(ar)
    for kar in kargs:
        print(kar , kargs[kar])
fun(1,2,3,4,5,6,name="ajay")

