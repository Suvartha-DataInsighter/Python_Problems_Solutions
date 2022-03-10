try:
	file=open('sample.xml')
	print(file)
	file.close()
except FileNotFoundError:
	print('Sorry the file we\'re looking for doesn\'t exist')
	#exit() #the exit() function will only execute if an exception is raised