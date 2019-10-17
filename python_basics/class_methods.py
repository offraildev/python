# Is Python call by reference or call by Value: Pyhton is neither, it is 
# "actually call by object" or "call by object reference"
# In Pyhton a variable is merely a name while other programming languages have it as box 
# with reference to a memory location.
# In pyhton everything is an object (two types mutable and immutable). When immutable 
# data types are passed as argument they are simply copied '
# and bound to a name within the scope of the function while for mutable the object 
# reference is passed so if the function modifies the values of
# the object the, it is reflected outside the function scope as well. Incase of augmentated 
# assignment eg: x += 1, the value is rebind to the name x.
# But if a immutable object contains a mutable obeject the mutable object can be modified.


# Module is a single python file while a package is a collection of such files. It can 
# be nested extensively but needs an additional __init__.py file
# to distinguish it from a directory and each sub package needs to have its own 
# __init__.py file
# Library itself in python doesn't have such meaning, but practically it stands for all 
# the core modules of python like I/O

# Class Variables: similar to static variables, attribute common to the entire class

class Employee:
    
    n_employees = 0  # need to initialize
    raise_amount = 1.1
    
    def __init__(self, first, last, pay): # self is the placeholder/variable for the entity 
        self.first = first           # that is created and is passed to the class blueprint automatically
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@kmail.com'
        
        Employee.n_employees += 1 # here it makes sense to use the Employee dot the class variable 
                                  # as the number of employees for each instance should not change or be overridden
        
    def fullname(self): # class action
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount  # here we can use either self(instance) or the class itself using self 
                                                 # adds flexibility in the sense that we can override the class variable 
                                                 # with the instance variable (makes sense in this case) 

# what happens here is, first the compiler checks if the instance has the attribute if 
# not then it 
# checks if the class or the class the instance inherits from has it 

print(f'Number of Employeees {Employee.n_employees}')
emp1 = Employee('Sajid', 'Mashroor', 5000)
emp2 = Employee('Shahid', 'Masood', 6000)
print(f'Number of Employees {emp1.n_employees}') # any of class or instance name can  access the class variable 

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.__dict__)
print(emp1.__dict__)

# since the raise amount attribute is common to all instances of the class the value remains same
# but if we do this

emp1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.__dict__) # class or instance dot __dict__ gives all the attributes and methods for class and 
print(emp1.__dict__)     # only attributes for instance in the form of a dictionary

# this changes things as it creates an instance attribute for emp1 but doesn't use the
#  class variable

# Class methods: These are used to modify class varibles, where instead of automatically
# passing a instance as in-case of a regular method we pass in the class automatically. 
# They are also used as an alternative constructor to provide multiple ways to create an instance.

# Static methods: In case of class methods and regular methods, the instance or the 
# class is passed automatically. But in this case no instance or class is passed and 
# works like a regular function. It is used when the method has logical association to 
# the class but does not depend on the instance or class variables.

# Pro-tip: Make a method static if it doesn't use any instance or class

class Employee:
    
    n_employees = 0  # need to initialize
    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        self.first = first           
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@kmail.com'
        
        Employee.n_employees += 1 
        
    def fullname(self): 
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount   
    
    # to create a class method just add classmethod decorator to regular method
    @classmethod     
    def set_raise_amnt(cls, amount): # cls is the convention for class, don't use the keyword class
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_string): # another way to create an instance, we can have multiple types of these
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay) # needs to return the created instance
    
    @staticmethod # staticmethod decorator to define the function 
    def is_weekday(day):
        if day == 5 or day == 6:
            return False
        return True


emp1 = Employee('Sajid', 'Mashroor', 5000)
emp2 = Employee('Shahid', 'Masood', 6000)
Employee.set_raise_amnt(1.05) # here we can use the instance as well but not recommended (doesn't make sense)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp3_string = 'John-Wayne-9000'
emp4_string = 'Little-Predetor-4000'
emp3 = Employee.from_string(emp3_string)
emp4 = Employee.from_string(emp4_string)

print(emp3.fullname())
print(emp4.fullname())
print(Employee.n_employees)

import datetime
my_day = datetime.date(2019, 9, 17)

print(Employee.is_weekday(my_day)) # or emp1.is_weekday(my_day), here class makes more sense though