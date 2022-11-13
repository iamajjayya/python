# # # # Decorators are a part of Python’s metaprogramming which are used to add additional functionality to existing code without altering the original structure at compile time.
# # # # 1 Function Decorators and 2. Class Decorators
# # # def strat_end_decorator(func):
# # #     def wrapper(*args ,**kwargs):
# # #         print("Strat")
# # #         result = func(*args,**kwargs)
# # #         print("End")
# # #         return result
# # #     return  wrapper()
# # #
# # #
# # #
# # # @strat_end_decorator
# # # def adds(x):
# # #     return x+10
# # #
# # # result= adds(5)
# # # print(result)
# # def python_pl(fun):
# #     def datascience():
# #         print("Python is a programming Language")
# #         fun()
# #         print("Datascience is a Technology")
# #     return datascience()
# # @python_pl
# # def ml():
# #     x=5
# #     print(10+x)
# # import functools
# # def repeat(num_of_times):
# #     def decorator_repeat(func):
# #         @functools.wraps(func)
# #         def wrapper(*args,**kwargs):
# #             result = func(*args,**kwargs)
# #             return  result
# #         return wrapper
# #     return decorator_repeat
# #
#
#
#
# @repeat(num_of_times=3)
# def greet(name):
#     print(f'Hello {name}')
# greet("AJAY")

class countclass:
    def __init__(self,func):
        self.func=func
        self.num_calls=0

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(f'This is excuted {self.num_calls}times')
        return self.func(*args ,**kwargs)


@countclass
def hello():
    print("hello")

hello()
hello()