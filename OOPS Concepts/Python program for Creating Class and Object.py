class Pigeon:
	species="bird" # creating class attribute
	def __init__(self,name,age):
		self.name=name ## instance attribute
		self.age=age
Jack=Pigeon("Jack",2) ## instantiate Pigeon class
Rooby=Pigeon("Rooby",1)
print("Jack is a {} ".format(Jack .__class__.species))
print("Rooby is a {}".format(Rooby .__class__.species)) # access the class attributes
print("{} is  {} years old ".format(Jack.name,Jack.age))
print("{} is {} years old ".format(Rooby.name,Rooby.age))
