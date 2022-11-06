import requests
import time
from bs4 import BeautifulSoup
import json

with open("itch-io-results.json",'w+') as file:
	base = '''{"response":[]	
}'''
	file.write(base)

def write_json(new_data, filename='itch-io-results.json'):
			with open(filename,'r+', encoding='utf-8') as file:
				file_data = json.load(file)
				file_data["response"].append(new_data)
				file.seek(0)
				json.dump(file_data, file, indent = 4)

def itchIoSearch(search):
		

	results = []
	
	url = "https://itch.io/search?q="+search
	startReq = requests.get(url)
	startSoup = BeautifulSoup(startReq.content, 'html.parser')
	
	titles = startSoup.find_all('a', class_='title game_link')
	
	for title in titles: 
		link = title.get("href")
		name = title.text.strip()
		
		titleCheck = name.lower()
		searchCheck = search.lower()
		if searchCheck in titleCheck:
			entry = {"title": name, 
					"URIs": link
					}
			write_json(entry)
		
			print(entry)
# ~ usage:
itchIoSearch("risk of rain")
		
