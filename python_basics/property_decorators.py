class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first}{last}@gmail.com'
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    
emp1 = Employee('John', 'James')

print(emp1.email)
print(emp1.fullname())

# Here, email depends on the first and last name provided in the constructor and if the 
# `self.first` or `self.last` is changed the email doesn't change

# The first name got changed but did not get reflected in the email change. The simpliest 
# way to solve this to have a method email that depends on the `self.first` and `self.last`
# to change/set the email but is not recomended as the already written code needs to be 
# changed from accessing the attribute to a method.

# Or We can make use of Property decorators (similar to Java Getter) to use the method but 
# access it like an attribute.

# Similarly we can do for fullname, now for the setting the fullname we use do the 
# following:
#     - have a decorator with func_name.setter over the function name and passing self and 
#     another value to be set

# Incase of defining a deleter we do the same but func_name.deleter has to be added and 
# only the self object needs to be passed and print out something during deletion to convey
# the object got deleted. 

# example

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = f'{first}{last}@gmail.com' # remove this 
    
    @property
    def email(self):
        return f'{self.first}{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')
        
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Object name deleted')
    
emp1 = Employee('John', 'James')
emp1.first = 'Don'

print(emp1.email) # since the method is used as a property
print(emp1.fullname)

# now let's use the setter and deleter
emp1.fullname = 'Sajid Mashroor'
print(emp1.fullname)
print(emp1.first)
print(emp1.last)

# now deleter
del emp1.fullname # to use the delter on the object use the built-in del keyword
print(emp1.fullname)