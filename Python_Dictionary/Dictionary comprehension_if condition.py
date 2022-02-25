def my_dict(s):
	dc={i:len(i) if len(i)>3 else 'less'for i in s}
	print(dc)
my_dict(['data','analysis','statistical','modelling'])
my_dict(['abc','avjhg','jhggd','owjksh'])


# Without using Dictionary Comprehension
# s=['data','analysis','statistical','modelling']
# my_dict={}
# for i in s:
# 	if len(i)>3:
# 		my_dict[i]=len(i)
# 	else:
# 		my_dict[i]='less'
# print(my_dict)


