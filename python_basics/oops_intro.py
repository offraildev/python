# Class instances or Entities: any abstract obejct characterised by some 
# attributes/parameters and actions that it can perform

# Class: Blueprint for an creating entities.
# attributes: instance variables (values different to each instance)
# methods: class functions

class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(id(emp1), id(emp2))
# each time the constructor is called a new object with a fresh memory and id

# emp1.name = 'Sajid'
# emp1.id = '101'

# emp2.name = 'Shahid'
# emp2.id = '102'

# print(emp1.name, emp1.id)
# print(emp2.name, emp2.id)

# instead of doing the abve steps we use a constructor/ init method

# instance variables are defined with self or the object keyword, but self is used by
# convention similar to  example: this.var
class Employee:
    
    def __init__(self, first, last, pay): # self is the placeholder/variable for the entity 
        self.first = first  # that is created and is passed to the class blueprint automatically
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@kmail.com'
        
    def fullname(self): # class action
        return f'{self.first} {self.last}'

emp1 = Employee('Sajid', 'Mashroor', 5000)
emp2 = Employee('Shahid', 'Masood', 6000)

print(emp1.fullname()) 
print(emp2.fullname()) # to call a class method we use the object name with a dot operator

# or Employee.details(emp1): **class name with object name passed as argument to method, 
# more readable