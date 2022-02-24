def insert_char(str1):
    str2=",".join(i+j for i,j in zip(str1[::2],str1[1::2]))
    print(str2)
str1="Working with string programs"
