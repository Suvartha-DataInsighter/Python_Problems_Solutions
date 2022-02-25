def my_dict(s,l):
	dict_zip={i:j for i,j in zip(s,l)}
	print(dict_zip.items())
my_dict(['data','analysis','statistical','modelling'],[5,8,6,9])
#print(dict_zip.items())