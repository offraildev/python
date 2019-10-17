# Creating Sub-classes: Allows us to inherit attributes and methods of our parent class. 
# Useful when we want to add some functionality and override the existing methods 
# without changing the original blueprint. Example: Employee parent - Developer child, 
# Manger child.

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
        
# create a child of Employee
class Developer(Employee):
    pass

dev1 = Developer('Jack', 'Ryan', 1000)
dev2 = Developer('John', 'James', 2000)

print(dev1.email)
print(dev2.email)
# here even though Developer class is not been clearly specified, it still inherits all the methods 
# and attributes from the parent class. It first checks if the child class contains the attribute if 
# not goes higher up the inheritance chain (Method resolution order). If the attribute or method is not found 
# in any class then it check in built in Object class. All classes in python inherit from the built in object 
# class (Base class)

print(help(Developer))

# Now let's add to the developer class a new raise amount and an added feature
class Developer(Employee):
    
    raise_amount = 1.1
    
    def __init__(self, first, last, pay, prog_lang): # needs all the data to be passed to the constructor
        super().__init__(first, last, pay) # the parent constructor can handle the inherited data
        # or Employee.__init__(self, first, last, pay) # this makes more sense in the case of multiple inheritance
        self.prog_lang = prog_lang # the new data is handled by our new object  
        

# now let's create another class child class
class Manager(Employee):
    
    raise_amount = 1.2
    
    def __init__(self, first, last, pay, employees=None): # deafult args should never be mutable datatypes
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print('Employee Already Exists with the Manager')
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("Employee doesn't exist with the Manager")
            
    def list_emps(self):
        if len(self.employees) != 0:
            for emp in self.employees:
                print(f'---> {emp.fullname()}')
        else: 
            print("No Employees found")
            

dev1 = Developer('Jack', 'Ryan', 1000, 'Pyhton')
dev2 = Developer('John', 'James', 2000, 'Java')

print(dev1.email)
print(dev2.email)

mgr1 = Manager('Corey', 'Schafer', 9000, [dev1])

print(mgr1.email)
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.list_emps()

# Pro-tip: Don't use mutable data types like lists or dictionaries as defualt arguments only immutable ones.

# is keyword is used to check if two variables refer to the same object

# isinstance checks if the specified object or varible is an instance of the class or could be a child class instance as well

# issublcass checks if the specified class is a sub-class of the class specified

dev3 = dev1

print(dev1 is dev3)
print(4 == 4) # to compare values use == but for varibles referring to same instance use is

print(isinstance(dev1, Developer))
print(isinstance(dev1, Employee))
print(isinstance(dev1, Manager))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

