#Write a program to reversing a list using slicing method
def reverse(l1):
	l2=l1[::-1]
	return l2
l1=[1,2,3,4,5,7,8,9]
print(reverse(l1))