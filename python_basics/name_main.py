# python has some special varibles that are set before any code is run 
# (note:in python everything is an object).

# __name__ special variable for a module/script  is set to "__main__" if 
# the script is run directly and to the script name if imported.  

# use case: if you want some of your code to be run directly or when imported

# first module
print("this part will run anyways")

def main():
    print("run directly")
    
if __name__ == "__main__":
    main()
else:
    print("Run on import in a seperate module")
    

# second module
import first_module

if __name__ == "__main__":
    print(f"Second modoule name {__name__}")