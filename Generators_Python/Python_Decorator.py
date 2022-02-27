def div_decorator(func):
	def inner(x,y):
		if y==0:
			return "we shouldnt divide with '0',give proper input"
		return func(x,y)
	return inner
def div(a,b):
	return a/b
print(div(5,2))