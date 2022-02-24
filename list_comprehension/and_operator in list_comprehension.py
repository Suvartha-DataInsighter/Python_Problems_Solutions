def logical_and(names):
	list1=[name for name in names if name.lower().endswith('a') and len(name)>3]
	print(list1)
logical_and(["shruthi","abhi","suvartha","chintu","priya"])