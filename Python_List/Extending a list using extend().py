#78.extending a list using extend()
# create a list
def myfun(n1,n2):
    num1 = [2, 3, 5]

# create another list to extend it
    num2 = [1, 4]
    num1.extend(num2)
    print('List after extend():', num1)
myfun(num1,num2)
