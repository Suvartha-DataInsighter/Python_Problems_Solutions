import xmltodict
import json
''' first of all ,we have to convert xml to python dictionary using the 'xmltodict' module
then python dictionary to json format......
To convert xml to python dictionary we use 'parse' method of the 'xmltodict' module,
and then to convert from python dictionary to json format we use 'dumps' method of the 'json' module'''
# xml='sample.xml'
# my_dict=xmltodict.parse(xml)
# json_data=json.dumps(my_dict)
# print(json_data)
# with open('sample.xml') as xml_file:
# 	my_dict=xmltodict.parse(xml_file.read())
# xml_file.close()
# json_file=json.dumps(my_dict)
# print(json_file)
xml='sample.xml'
with open('sample.xml') as xml_file:
 	my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_string=json.dumps(my_dict,indent=2)
print(json_string)
jsonFile=open("json_file1.json","w")
jsonFile.write(json_string)
jsonFile.close()