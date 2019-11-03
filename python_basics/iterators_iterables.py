# iterator: object that has __iter__ and __next__ dunder methods implemeted and must raise
# StopIteration exception when exhausted, gets exhausted
# iterable: object we can loop over, has __iter__ method implemeted 
# generator: also and iterator, has the __iter__ and __next__ method automatically
# implemeted and can be used in the form of a function as well
nums = [1, 2, 3]

for n in nums:
    print(nums)

print(dir(nums))

# list is an iterable but not iterator, has not __next__ method

# when the for is run on iterable it calls the ojects __iter__ method
# this return an iterator obejct which we can then invoke the next method on it

# the above code is same as 
i_nums =  iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# for loop takes care the exception in this way

# create custom Range Iteartor class
# __iter__(): method needs to return a an iterator obejct 
# (has __iter__ and __next__ implemeted) or return itself and __next__ implemeted
#  to break the loop 
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):  
        return self

    def __next__(self):
        current = self.value
        
        if current >= self.end:
            raise StopIteration
        self.value += 1
        return current 

for i in MyRange(0,9):
    print(i)


# can do the above code more concisely using generator function
def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for i in my_range(0, 9):
    print(i)

# iterators need not end 
# example

def my_range(start):
    current = start
    while True:
        yield current
        current += 1

