# # # # # # #iterables list
# # # # # # lst =[1,2,3,4,5]
# # # # # # # for i in lst:
# # # # # # #     print(i)
# # # # # # lst1=iter(lst)
# # # # # # lst1
# # # #
# # # # def mygenerator():
# # # #     yield  1
# # # #     yield 2
# # # #     yield 3
# # # # g=mygenerator()
# # # # # for i in g:
# # # # #     print(i)
# # # # # value =next(g)
# # # # # print(value)
# # # # # print(sum(g))
# # # def countdown(num):
# # #     print("Starting")
# # #     while num > 0:
# # #         yield num
# # #         num-=1
# # # cd =countdown(4)
# # # value=next(cd)
# # # print(value)
# # # print(next(cd))
# # # print(next(cd))
# # # print(next(cd))
# # #
# # # cd
# # #
# # #
# # import sys
# # def first(n):
# #     nums=[]
# #     num=0
# #     while num < n:
# #         nums.append(num)
# #         num+=1
# #     return nums
# # def first_generator(n):
# #     num =0
# #     while num < n:
# #         yield num
# #         num+=1
# # print(sys.getsizeof(first(1000)))
# # print(sys.getsizeof(first_generator(1000)))
#
#
# def fibonacci(limit):
#     a,b=0,1
#     while a < limit:
#         yield a
#         a,b=b,a+b
# fib = fibonacci(10)
# for i in fib:
#     print(i)

mygenerator =(i for i in range(10) if i%2==0)
# for i in mygenerator:
#     print(i)
print(mygenerator)
