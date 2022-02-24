import re
str1="this is an example for meta characters in RegX"
result=re.findall("[ia]",str1)
print(result)