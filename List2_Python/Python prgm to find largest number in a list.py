def max_num(l1):
	max=l1[0]
	for x in l1:
		if x>max:
			max=x
	return max
l1=[10,20,30,24,33,64]
print(max_num(l1))