#Write a program to multiply list of elements
def multiply_list(l1):
	result=1
	for x in l1:
		result =result*x
	return result
l1=[1,2,3,4]
print(multiply_list(l1))