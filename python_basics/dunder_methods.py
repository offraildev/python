# Special methods (dunder/magic): These allow us to emulate built-in behaviour and 
# functionalities in python. They are surrounded by double underscore (__) ,i.e dunder.
#  Using these we can change pre-existing behaviour of methods, override them and add some new functionality.

# Some common Special methods:
# Always implement these: __str__ and __repr__
# __str__: this is used to display a more readable representation of the object and is intended to be shown 
# to the end-user.

# __repr__: this is supposed to be an unambiguous  representation of the object and to be used for logging 
# or debugging and meant to be seen by other    developers

# for example 
print(1+2)
print('a'+'b')

# Here the beaviour of the addition operator changes depending on the type of object provided

class Employee:
    
    raise_amount = 1.05
    
    def __init__(self, first, last, pay): 
        self.first = first           
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@kmail.com'
 
    def fullname(self): # class action
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
        
    def __str__(self): 
        return f"{self.fullname()} - {self.email}"
    
    #always try to implement this: the str() falls 
    #back to this even if __str__ is not implemented
    def __repr__(self): 
        return f"Employeeyee({self.first}, {self.last}, {self.pay})"      
    
    # some other ones 
    # takes only the object
    def __len__(self):
        return len(self.fullname())
    
    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employee('John', 'Wick', 3000)
emp2 = Employee('Sajid', 'Mashroor', 6000)

# Good rule of thumb:
# For `__repr__()`: print out something that can be copied into python and recreate 
# the object.

print(emp1)
# printing the object uses the __str__, incase not implemented 
# the __repr__ is used

# using the object
print(emp1.__str__())
print(emp1.__repr__())

# using the built in functions
print(str(emp1))
print(repr(emp1))

print(emp1+emp2)
print(len(emp1))

# Similar to `str.__len__()` `int.__add__()` all objects can override these built-in 
# methods for objects that inherit from Object class (meaning all objects ), but these 
# need to defined properly

# If for some case the special method is not defined, the we can return NotImplemented 
# exception to tell the parent to take care of the method definition, or some other 
# class down the inherit chain. 

# Link to other special methods in python docs: 
# https://docs.python.org/3/reference/datamodel.html#special-method-names