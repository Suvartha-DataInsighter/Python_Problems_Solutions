#Python program For simple Calculator
def addition(n1,n2):
	return n1+n2
def substraction(n1,n2):
	return n1-n2
def multiplication(n1,n2):
	return n1*n2
def division(n1,n2):
	return n1/n2
def modulo_div(n1,n2):
	return n1%n2
# print("please select operation -\n" \
# 	"1.addition\n" \
# 	"2.substraction\n" \
# 	"3.multiplication\n" \
# 	"4.division\n" \
# 	"5.modulo_div\n" )

select=int(input("Select an operation from 1,2,3,4,5:"))

if select ==1:
	print(addition(10,20))
elif select ==2:
	print(substraction(10,20))
elif select ==3:
	print(multiplication(10,20))
elif select ==4:
	print(division(10,20))
elif select ==5:
	print(modulo_div(10,20))
else:
	print("Invalid selection")