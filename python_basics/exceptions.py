# deal with errors in a specified way
try:
    # try block throws an exception when an error occurs 
    f = open('test.txt')
    #var = bad_var
    
    # user defined excetion, using raise keyword
    if f.name != 'test':
        raise Exception
except FileNotFoundError as e:
    # try to make your exceptions as spefic as possible,
    # helps in debugging 
    print(f"Sorry file doesn't exist, {e}")
    print(f)
except NameError as e:
    print(e)
except Exception as e:
    # more general error, specify at end, 
    # else will be called only and not the speficic error
    print(f"Sorry something went wrong, {e}")
else:
    # if try doesn't throw an  exception then use this
    contents = f.read()
    f.close()
    print(contents)
finally:
    # runs regardless of exception, best to release memory 
    # or resources
    print('Executing finally...')