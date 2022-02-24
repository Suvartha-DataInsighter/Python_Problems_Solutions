# create a list
def myfun(l1,l2):
# create another list to extend it
    l1.extend(l2)
    print('List after extend():', l1)
l1=[2, 3, 5]
l2 = [1, 4]
myfun(l1,l2)

