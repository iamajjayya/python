#errors and exception
#raise exception
#x = int(input(" enter a number"))
# if x<0:
#     raise Exception("Enter a positive number")
#assertion
#assert ( x>=0) ,"x shoud be greater than or equal to 0"
#try and except
# try:
#     a = 12 /0
# except Exception as e:
#     print(e)
#
# try:
#      a=10+"hello"
#      b=2 /0
# except Exception as e:
#     print(e)
# else:
#     print("No error")
# finally:
#     print("alway show this statement")
#negative value
class negativevalueerror(Exception):
    pass
def textvalues(x):
    if x <=0:
        raise negativevalueerror("Value is negative")
try:

 textvalues(-4)
except negativevalueerror as e:
    print(e)

