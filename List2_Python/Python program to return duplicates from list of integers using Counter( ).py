from collections import Counter
l1=[1,2,3,1,2,3,4,5,4,7,6,7,8,8,9]
duplicates=Counter(l1)
l2=list([i for i in duplicates if duplicates[i]>1])
print(l2)