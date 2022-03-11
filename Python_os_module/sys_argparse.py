import getopt,sys
import argparse
import os
from pathlib import Path
from os import path
import re

print("The script has the file name %s"%(sys.argv[0]))
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='for help')
args = parser.parse_args()
print(args.i)
#i=input("enter file path")
def my_file_existence():
	reg_ex=re.findall('.xml',i)

	if str(path.exists('D:/Myfiles')) :
		#if str(path.exists('D:/Myfiles'))

	   	print ("File existed")
	else:
	   	print("The file not founded")

	  

if __name__== "__main__":
   my_file_existence()
