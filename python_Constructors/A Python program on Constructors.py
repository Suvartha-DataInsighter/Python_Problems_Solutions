## Constructors are generally used for Instantiating the objects,
#In Python __init__() method is called constructorand it is always called when the object is created
#Syntax for Constructor Declaration
# def __init__(self):
# 	#body of the constructor

#ex1.Parameterised Constructor
class addition:
	 n1=0
	 n2=0
	 result=0
	 def __init__(self,n1,n2,result):
		  self.n1=n1
		  self.n2=n2
		  self.result=result
	 def display(self):
		 print("First number=" +str(self.n1))
		 print("Second number=" +str(self.n2))
		 print("additionof two numbers =" +str(self.result))
	 def calculate(self):
		 self.result=self.n1+self.n2
a=addition(20,30,20+30)
a.display()
a.calculate()