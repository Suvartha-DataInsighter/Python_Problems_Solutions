# The __del__() method is a known as a destructor method in Python. It is called when all references to the object have been deleted 
# when an object is garbage collected. 
# syntax :
# def __del__(self):
#    body of destructor

# Python program to illustrate destructor
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
del obj
