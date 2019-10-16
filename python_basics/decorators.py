from functools import wraps

def add_wrapper_with_style(style):
    def add_wrapper(func):
        @wraps(func)
        def wrapper():
            return f"a {style} wrapped box of {func()}"
        return wrapper
    return add_wrapper

def add_wrapper(func):
    def wrapper(a, b):
        return f"a wrapped box of {func(a,b)}"
    return wrapper
 
@ add_wrapper
def plus(a,b):
    return a+b

@ add_wrapper_with_style('horribly')
def new_bike():
    return "a brand new bike"


print(plus(4,5))
#print(new_bike()