def my_func(my_l1):
	even_list=list(filter(lambda x :(x%2==0),my_l1))
	return even_list
my_l1=[12,13,141,15,16,17,18,23,24,226,25,27,65,66,35,34]
print(my_func(my_l1))