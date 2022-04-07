import argparse
from email import parser
import sys
import os.path
import getopt
import xml.etree.ElementTree as ET 

def file_path():
    # argv = sys.argv[2]
    # print(argv)
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",dest="myFile",help="Open specified file")
    args=parser.parse_args()
    path=args.myFile
    # file=open(path)
    # print(file.read())
    # file.close()

    if os.path.exists(path):
        print ("File existed")
        
    else:
        print ("File not existed")
        exit()
    filename = os.path.splitext(path)
    file_extension='.xml'
    if file_extension in filename:
        print("it is an xml file")
        tree = ET.parse(path) 
        root = tree.getroot() 
        print(root[0].attrib) 
    else:
        print("it is not an xml file")
        exit()  
if __name__=='__main__':
    file_path()
    