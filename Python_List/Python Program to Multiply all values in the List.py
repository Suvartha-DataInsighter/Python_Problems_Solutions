def multiply(mylist):
    result = 1 # multiply elements one by one
    for x in mylist:
        result= result*x
    return result
list1=[1,2,3]
list2=[2,3,4]
print(multiply(list1))
print(multiply(list2))