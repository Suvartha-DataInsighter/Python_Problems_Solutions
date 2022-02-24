#python prgm to extract comma-seperated words in a given string without using split()
def splitting_string(string):
	for each in string:
	    if(each==","):
		    pass
	    else:
		    print(each,end=" ")
string="this,is,a,comma,seperated,string"
splitting_string(string)