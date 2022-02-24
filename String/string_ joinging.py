def str_join(str1):
    str2="@".join(str1[i:i+3] for i in range(0,len(str1),2))
    print(str2)
str1="Working with string programs"
str_join(str1)
