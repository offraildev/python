# Pythonic: Following conventions and coding styles of python language to write clean and readable code
# duck typing and Easier to ask for forgiveness than permission (EAFP)

# if it qucks and acts like a duck it is a duck, we don't care if it is the thing or not 
# but we care if it can do the thing or not   
class Duck:

    def quack(self):
        print("quack, quack")

    def fly(self):
        print("flap, flap")

    
class Person:

    def quack(self):
        print("I'm quacking like a duck")
    
    def fly(self):
        print("I'm flapping like a bird")


def quack_n_fly(thing):
    # non-pythonic
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("thing has to be a Duck type")

    # look before you leap (non-pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

        if callable(thing.fly):
            thing.fly()

    # pythonic: we just do the thing want to do and ask for 
    # forgiveness if an error occurs by handling it as an exception
    try: 
        thing.fly()
        thing.quack()
    except AttributeError as e:
        print(e)

d = Duck()
quack_n_fly(d)

p = Person()
quack_n_fly(p)


# examples of pythonic way 

people = {'name': "Sajid", 'age': 25, 'height': 5.7}
people = {'name': "Sajid", 'age': 25}

# LBYLP
if 'name' in people and 'age' in people and 'height' in people:
    print("Name: {name}, Age :{age}, Height: {height}".format(**people))
else:
    print("some key is missing")

# pythonic
try:
    print("Name: {name}, Age :{age}, Height: {height}".format(**people))
except KeyError as e:
    print(f"Missing key {e}")


my_list = [1,23,35,6,2,6]

# non-pythonic
if len(my_list) >= 6:
    print(my_listp[5])
else:
    print("that index doesn't exist")

# pythonic
try:
    print(my_list[5])
except IndexError as e:
    print(e)

# why being pythonic is necessary: this is imperitive in the condition that 
# when the if statement doesn't throw and error and else is executed the error 
# may never be caught

# callable: calllable is something that can be callled like and object.
# built-in callable() takes in only one argument, so to check for method try 
# obj_name.method_name (don't use (), else it will be callled) 

# hasattr: check if the object has the attribute or not