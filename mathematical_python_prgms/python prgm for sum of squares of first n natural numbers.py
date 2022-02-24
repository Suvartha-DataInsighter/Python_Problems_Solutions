#python prgm for sum of squares of first n natural numbers
def squaresum(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+(i*i)
	return sum
print(squaresum(4))