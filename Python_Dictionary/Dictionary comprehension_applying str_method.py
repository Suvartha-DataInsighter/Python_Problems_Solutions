def my_dict(s,l):
	dict_zip={i.upper():j*2 for i,j in zip(s,l)}
	print(dict_zip)
my_dict(['data','analysis','statistical','modelling'],[5,8,6,9])

