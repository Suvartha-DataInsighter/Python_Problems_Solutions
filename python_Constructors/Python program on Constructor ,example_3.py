class Employee:
	def __init__(self,Name,Salary):
		self.Name=Name
		self.Salary=Salary
	def display(self):
		print("Employee Name:",self.Name)
		print("Employee Salary:",self.Salary)
e1=Employee("Shruthi",25000)
e2=Employee("Abhi",35000)
e3=Employee("Naveen",40000)
e1.display()
e2.display()
e3.display()

