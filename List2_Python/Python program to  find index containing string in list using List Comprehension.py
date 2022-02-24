#The task is to find the index containing string by using list comprehension
l1=["shruthi","abhi",21,20,"Chintu",16,"Karthik"]
print(l1)
#List comprehension
print([l1.index(i) for i in l1 if(type(i) is str)])
#list comprehension that displays strings
print([i for i in l1 if(type(i) is str)])