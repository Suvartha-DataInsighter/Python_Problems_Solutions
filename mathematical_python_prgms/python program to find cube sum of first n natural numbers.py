def sumofseries(n):
	sum=0
	for i in range(1,n+1):
		sum+=i*i*i
	return sum
print(sumofseries(5))