# List Comprehension is basically creating lists based on the existing iterables
#syntax:list=[expression for item in iterable (if conditional)]
def even_list(a):
	b=[i for i in a if(i%2==0)]
	print(b)
a=[1,2,3,4,5,6,7,8]
even_list(a)
