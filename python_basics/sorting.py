# Sorting tips:
# use built-in sorted function: this is not an in-place sort.
sorted(obj, key=func, reverse=True)

# to sort a list in-place.
my_list.sort()

# other objects may have such methods

# the key argument takes in a function to transform the inputs 
# and then sort the iter items. The function can be a lambda or 
# a normal function which returns a transformed value.
my_list = [1, 2, 3, -4, -5, -6]
sorted(my_list, key=abs,reverse=True)


# Example for sorting a list of custom instances of the same class.
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

emp1 = Employee("sajid", 25, 5000)
emp2 = Employee("shahid", 27, 6000)
emp2 = Employee("animesh", 25, 8000)

emps = [emp1, emp2, emp3]

def get_name(emp):
    return emp.name

def get_age(emp):
    return emp.age

# specify function, don't call it and the item is passed by itself.
sorted(emps, key=get_name, reverse=True)
sorted(emps, key=get_age)

# using attrgetter

from operator import attrgetter
sorted(emps, key=attrgetter("name"))
sorted(emps, key=attrgetter("age"))