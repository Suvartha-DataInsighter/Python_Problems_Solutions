l1=[1,2,3,1,2,3,4,5,4,7,6,7,8,8,9]
new_list=[]
for i in l1:
	n=l1.count(i)
	if n>1:
		if new_list.count(i)==0:
			new_list.append(i)
print(new_list)