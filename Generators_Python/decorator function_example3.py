def func1():
	print("hi Iam function 1")
def func2(func):
	print("Hi I am function2,now iam calling function 1")
	func()
func2(func1)