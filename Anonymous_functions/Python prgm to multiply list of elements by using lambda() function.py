import functools
from functools import reduce
l1=[1,2,3,4]
l2=[1,3,5,7]
result1=reduce((lambda x,y:x*y),l1)
result2=reduce((lambda x,y:x*y),l2)
print(result1)
print(result2)
