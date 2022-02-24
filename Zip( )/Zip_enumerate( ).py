# Python zip_enumerate()
def enumerate_zip(names,ages):
    for (name, age) in enumerate(zip(names, ages)):
        print(name, age)
names = ['Rakesh', 'Prince', 'Charles']
ages = [24, 50, 18]
enumerate_zip(names,ages)
 
# The result would give index,tuple()