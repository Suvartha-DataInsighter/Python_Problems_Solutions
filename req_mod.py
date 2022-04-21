
import requests
from requests.exceptions import HTTPError
from pprint import pprint
import json

def main():
	url='http://192.168.27.119/mmp-api/api/recordings?tz=Asia%2FKolkata&page=1&timeout=60&hostUrl=http%3A%2F%2F192.168.27.119%2F&box_name=DN-FMT01-1119&access_token=RE4tRk1UMDEtMTExOXwyMDIyLTA0LTIwIDEzOjU0OjEx'
	r = requests.get(url)
	print(r)
	json_txt_data = r.json().get("data")
	dict1 = {}
	for index, value in enumerate(json_txt_data):
		json_data={'callsign':json_txt_data[index].get("callsign"),
                   'rec_start':json_txt_data[index].get("rec_start"),
                   'rec_end':json_txt_data[index].get("rec_start"),
                   'chan_id':json_txt_data[index].get("chan_id")}
		# dict1.update(json_data)
		# print(dict1)
		dict2={}
		dict2.update(json_data)
		if dict2['chan_id'] not in dict1:
			dict1[dict2['chan_id']]=[]
			dict1[dict2['chan_id']].append(dict2)
		else:
			dict1[dict2['chan_id']].append(dict2)
	
	print(json.dumps(dict1))
		
		
if __name__ == "__main__":
	main()