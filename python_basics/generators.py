# generator using a yield keyword
# generators don't load the entire iterable in memory 
#but yields it one at a time when asked using next keyword
def square(nums):
    for i in nums:
        yield i*i
        
my_nums = [i for i in range(1, 6)]
squared = square(my_nums)

# computes the values when next is called
# gives a StopIteration exception when generator is exhausted
next(squared)

# workaround for this is to use a for loop on the generator object
for i in my_nums:
    print(i)

# generator using parenthesis
squared = (i*i for i in my_nums) 