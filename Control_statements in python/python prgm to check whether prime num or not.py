n=int(input("enter any num:"))
if n>1:
	for i  in range(2,n):
		if(n%i==0):
			print(n,"it is not a prime num")
			break
		else:
			print(n,"it is a prime number")
else:
	print(n,"it is not a prime number")