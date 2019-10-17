# first class functions: A Programming language is said to have first class functions if it treats functions 
# as first class citizens (objects).
    
# first class citizens: In the context of a programming language, it is an entity which supports all the 
# operations that are available to other entities including being passed as an argument to function, assigned 
# to a variable, modified and being returned from a function.

# higher order functions: functions that can take function as an argument or return a function, in contrast 
# to first order functions which can't do the same. example: map function

# example

def square(x):
    return x**2

# function without () is just the function entity 
f = square  # () executes the function
print(square)
print(f)
print(f(6))

# example: passing a function as an argument to a function
def my_map(func, arg_list): # func placeholder or variable now holds the function object
    result = []
    for item in arg_list:
        result.append(func(item)) # here the function object just gets replaced and python in pass by object
    return result

print(my_map(square, [1,2,3,4,5]))

# example returning functions from functions
def html_tag(tag):
    
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
        
    return wrap_text 

print_h1 = html_tag('h1') # initialize with h1
# when the above line gets executed html_tag function gets executed an returns the wrap_text func gets 
# returned and is assigned to the variable but nothing happens unless the variable is executed and while it 
# still hasn't been executed it stores the data that was passed to it.
# this is used to modifiy an existing function
print(print_h1)
print_h1('Test Headline') # modify the function 
print_h1('Another Headline')

print_p = html_tag('p') # initialize with p
print_p('Test Paragraph') # modify the function 

# closures: in simple terms, it is an inner function that remembers and has access to variables
# in the local scope the inner function was defined in even after the outer function has finished 
# executing.

def outer_func(msg):
    message = msg
    
    def inner_func():
        # here message is a free varible, i.e, the inner function has access to it but 
        # is not defined within its scope
        print(message)
        
    return inner_func

outer_func('hi')

# logging with closures
import operator 
import logging
from functools import reduce
# here .log is the log file extension
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    
    def log_func(*args): # *var in function def is for unknown set of args
        logging.info(
            f'Running {func.__name__} with arguments {args}') # func.__name__ gives the function name
        print(func(*args)) # unpack the arguments with * in function execution
        
    return log_func

def add(*args):
    # return sum(args)
    return reduce(operator.add, args) # or try __add__

def sub(*args):
    return reduce(operator.sub, args) # or try __sub__

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(5, 7, 7, 3)
sub_logger(7, 5, 7, 8)

# Reduce and Filter Functions

reduce(lambda x, y: x-50, a)

# reduce function: higer order function, used to apply a given function to all the elements in 
# a list, defined in the functools module

# working: the first two elements are picked and the supplied to the function and then the result 
# is then compared with the next result and so on untill the container is empty

from functools import reduce

a = list(range(1,6))
greatest = reduce(lambda x,y: x if x>y else y, a)
print(greatest)

# filter function: higher order function to filter out elements of a list for which the function 
# return true.

# example: return palindrome strings
strings = ['adam', 'malayalam', 'telegu', 'samas', 'a']
print(list(filter(lambda s: s[::-1] == s, strings)))

# Lambda and List Comprehension

# lambda keyword in python is used to create anonymous functions, it can take multiple arguments \
# but has only one expression
func = lambda *x: sum(x)
func(2,4,7)

# list comprehension:
[print(i) for i in range(10)] # one for loop 
[print(i*j) for j in range(2) for i in range (5)] #inner-outer
[print(i) for i in range(10) if i > 5 if i < 8] # only if (nested also) conditionals and for loop
[print('Even') if i%2 else print('Odd') for i in range(10)] # if and else on the left

# Decorators

# decorator: It is a function that takes a function as an argument and adds some functionality 
# to the function without changing the source code of the original function

# function decorators 

def decorator_func(original_func):
    
    # this adds some functional to the original function
    def wrapper_func(*args, **kwargs): # so that we can pass multiple args and kwargs or none at all 
        print(f'wrapper executed this before {original_func.__name__}')
        original_func(*args, **kwargs)
    
    return wrapper_func

@decorator_func
def display():
    print('Display function ran')
    
# the above syntax is same as decorator with original function as argument and assigned to original 
# function, i.e, adds functionality to the function without changing the source code 
# display = decorator_func(display)
    
@decorator_func    
def display_info(name, age):
    print(f'Display name: {name} and age: {age}')
    

display()
display_info('sajid', 23)     

# similarly we can have decorator class
class decorator_class(object):
    
    # here the original function is passed to the constructor (__init__ method)
    def __init__(self, original_func): 
        self.original_func = original_func
    
    # here the __call__ method acts as  the wrapper function
    def __call__(self, *args, **kwargs):
        print(f'Wrapper class executed this before {self.original_func.__name__}')
        self.original_func(*args, **kwargs)
        
        
@decorator_class
def display():
    print('Display function ran')

# the above syntax is same as: 
# display = decorator_class(display)
    
@decorator_class  
def display_info(name, age):
    print(f'Display name: {name} and age: {age}')
    
display()
display_info('sajid', 25)      

# some decorator usecases:
# logging
from functools import wraps

def my_logger(original_func):
    import logging # set-up log file
    logging.basicConfig(filename=f'{original_func.__name__}.log', level=logging.INFO)
    
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Running {original_func.__name__} with args: {args} and kwargs: {kwargs}')
        return original_func(*args, **kwargs)
    
    return wrapper

def my_timer(original_func):
    # set up timer
    import time
    
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time()
        print(f'{original_func.__name__} ran in {t2-t1} seconds')
        return result
    
    return wrapper

# we can stack decorator functions like this
@my_logger
@my_timer  # inner first
def display_info(name, age):
    print(f'Display name: {name} and age: {age}')
    
# this is same as:  display_info = my_logger(my_timer(display_info)) which equates to 
# display_info = my_logger(wrapper)
# to avoid this we will decorate the wrapper with wraps from functools

display_info('sajid', 25)

# decorators with arguments

def prefix_decorator(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args, **kwargs): 
            print(f'{prefix} Executed before {original_func.__name__}')
            result = original_func(*args, **kwargs)
            print(f'{prefix} Executed After {original_func.__name__}')
            return result
        return wrapper_func
    return decorator_func

@prefix_decorator('Log:')
def display_info(name, age):
    print(f'Display name: {name} and age: {age}')
    

display_info('sajid', 25)
display_info('Shahid', 27)