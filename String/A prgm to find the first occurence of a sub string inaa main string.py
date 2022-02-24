string=input("enter the string:")
sub_str=input("enter the substring:")
n=string.find(sub_str,0,len(string))
if n==-1:
    print('sub string is not found in the given string')
else:
    print('sub string found at position:',n+1)