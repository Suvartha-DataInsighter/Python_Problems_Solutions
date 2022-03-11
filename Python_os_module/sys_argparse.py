import getopt,sys
import argparse
import os
from pathlib import Path
from os import path
import re




#i=input("enter file path")
def my_file_existence(file_path):
	file_path=str(path.exists("D:/Myfiles/sample.xml"))
	if file_path :
		print ("File existed")

		# store file path in a variable
		# read filename and extension from filepath
		# using os module
	 	# check extenstion against xml
	
		filename, file_extension = os.path.splitext('D:/Myfiles/sample.xml')
		filename='D:/Myfiles/sample.xml'
		file_extension='.xml'

		if file_extension in filename:
			print("The existed file is an xml file only")
		else:
			print("The existed file is a different file")

	else:
	   	print("The file not founded")

	  

if __name__== "__main__":
	print("The script has the file name %s"%(sys.argv[0]))
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', help='for help')
	args = parser.parse_args()
	print(args.i)
   	
my_file_existence(file_path=str(path.exists("D:/Myfiles/sample.xml")))