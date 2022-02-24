str1=[["sap","sas","spss"],["python","sql","excel"],["java","r","css"]]
str2=[y for x in str1 if len(x)>3 for y in x]
print(str2)


text=['fooba', 'Madrid', 'Houston']
text_2 = [y for x in text for y in x if len(y)>4]
print(text_2)
