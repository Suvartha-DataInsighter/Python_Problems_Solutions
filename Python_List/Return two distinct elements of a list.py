def distinct(l1):
    return [i for i in l1 if l1.count(i)==1]
print(distinct([1,2,3,1,2,3,4,5,6,3,6]))