from datetime import timedelta, datetime
import time
import argparse 
# readDataFromFile() --- reading data from .txt file
# formatData() --- adding given minutes 
# writeDataInFile() -- writing data inside .txt file
# all methods should called from main only....
def main():
	# parser=argparse.ArgumentParser()
	# parser.add_argument(dest="myFile",help="Open specified file")
	# args=parser.parse_args()
	# path=args.myFile
	
	 with open("D:/Myfiles/caption_missing_tf.txt","r")as file:
	 	lines = file.readlines()[2:]
	 	new_list = []
	 	for line in lines:
	 		words = line.split("\t")
	 		date_time = words[0]
	 		date_time1=datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')
	 		new_datetime1 = date_time1 + timedelta(minutes=30)
	 		str_datetime=new_datetime1.strftime("%Y-%m-%d %H:%M:%S")
	 		words[0] = str_datetime
	 		line = "\t".join(words)
	 		new_list.append(line)
	 		
	 		with open('file2.txt', "w") as writing_file:
	 			for m_list in new_list:
	 				writing_file.writelines(m_list)
	 				
if __name__ == "__main__":
	main()
