#The task is to find the index containing string
l1=["shruthi","abhi",21,20,"Chintu",16,"Karthik"]
print(l1)
for i in l1:
	if(type(i) is str):
		print(l1.index(i))