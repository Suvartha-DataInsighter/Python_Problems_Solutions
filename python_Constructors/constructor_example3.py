class A:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display_me(self):
		print("This is {},and I am {} years old".format(self.name,self.age))
a=A("Aadhya",7)
a.display_me()