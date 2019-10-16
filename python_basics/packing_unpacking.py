## list or tuples

# unpacking: unpack an iterable 
def sum(a, b, c):
    return a + b + c

my_list = [4, 5, 8]

print(sum(*my_list)) # * with iterable unpacks it

# packing: use din function (unknown number of parameters)
def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(sum(1,23,5,6,8)) # don't know how many items to give
print(sum(1,5))
print(sum(*[1,2,3,5,8]))

## Dicts

# unpacking: unpack an dict (named iterable) 
def sum(height, weight):
    return height/weight

my_list = {'height': 5, 'weight': 60}

print(sum(**my_list)) # * with iterable unpacks it

# packing: packing unknown number of keywords
def p_result(**kwargs):
    for k in kwargs:
        print(kwargs[k])


p_result(age=5, weight=6)