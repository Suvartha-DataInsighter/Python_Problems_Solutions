num=int(input("enter num to divide:"))
l_range=list(range(1,num+1))
divisorlist=[]
for number in l_range:
    if num%number==0:
        divisorlist.append(number)
print(divisorlist)