# strip(): is used to delete all the leading and trailing characters
def str_strip(string):
	print(string.strip("_"))
	print(string.lstrip("_"))
	print(string.rstrip("_"))
string="______Programming Language_______"
str_strip(string)
