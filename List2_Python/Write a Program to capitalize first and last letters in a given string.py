def cap_first_last_letters(str1):
	str1=str1.title()
	result=" "
	for word in str1.split():
		result+=word[:-1]+word[-1].upper()+" "
	return result[:-1]
print(cap_first_last_letters("hello world"))