# context managers: efficiently manage resources, takes care of the resource's teardown 
# automatically (eg: file is closed automatically). Even if nested code raises an error 
# the context manager will take care of the resource teardown.
# Example use-cases: automatically closing databases, acquiring and releasing locks.

# custom context managers: using class (simple example to replicate already existing 
# feature of file open and close using open function context manger).


class OpenFile:
    """
    Open file with given name and mode.
    
    Args:
        filename (string): path to file.
        mode (string): mode to use while opening file.
    """
    
    def __init__(self, file_name, mode): 
        # set state
        self.file_name = file_name
        self.mode = mode
        
    def __enter__(self):
        """Return the file object for specified file."""
        
        # return an object that you want to work with
        self.file = open(self.file_name, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        # the other args are there to access the error data if we raised and exception
        # take care of the teardown
        self.file.close()
        

# here first the class constructor is run with the initial values, then we 
# step into the __enter__ method to return a file object which is assigned 
# to f, finally the after operating on the file object when we reach the new 
# indent we step into the __exit__ method and the file is closed 
# automatically for us.    
with OpenFile("sample.txt", "w") as f:
    f.write("this is a test file")

# check if file got closed
print(f.closed)

 
# custom context manger: using a generator function and 
# contextlib.contextmanager decorator
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        yield file
    except Exception as e:
        print(e)    
    finally: 
        # this makes sure even if there is and error the file 
        # is closed at the end
        file.close()

# here for the clode above the first two lines are similar to the __init__ 
# and __enter__ methods the file obect is yielded and the new indent 
# is reached after the with statement the file is closed. Ideally we should 
# have a try/catch surrounding the set-up and the yield lines  
with open_file("sample.txt", "w") as f:
    f.write("lorem ipsum, dolor sit amet.")

# check if file got closed
print(f.closed)    

# more practical context manager example: change to a directory, 
# do something, change back to cwd, do this again for another directory
import os

# cwd = os.getcwd()
# os.chdir("/home/nbuser/library/hangman")
# # the above two lines are set-up 
# print(os.listdir()) # do something 
# os.chdir(cwd) # teardown

# cwd = os.getcwd()
# os.chdir("/home/nbuser/library/data_files")
# print(os.listdir()) # do something 
# os.chdir(cwd) # teardown

# the above lines can be done using the context manager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield # can just yield if no value to yield 
    except Exception as e:
        print(e)
    finally:
        os.chdir(cwd)
        
with change_dir("/home/nbuser/library/hangman"): 
    # no as object since nothing yielded
    print(os.listdir())
    
with change_dir("/home/nbuser/library/data_files"):
    print(os.listdir())

# difference between yeild and return: 
# The yield statement suspends function execution and sends back a 
# value to the caller, while saving the state and later resuming, 
# meaning the whole generator function itself can be resumed after 
# the returned value is obtained. While the return statement just 
# suspends function execution and send back a value to the caller.

# Note: When no value is to be sent back, just yield or return is enough.
# Yield with no value sends back a generator and return sends back a NoneType

def multiply_by_3(x):
    num = x * 3
    print(num)
    yield   

type(multiply_by_3(9))

def multiply_by_3(x):
    num = x * 3
    print(num)
    return 

type(multiply_by_3(9))
