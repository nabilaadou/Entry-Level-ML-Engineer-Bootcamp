from bs4 import BeautifulSoup as bs
import requests
import csv

response = requests.get("https://data.1337ai.org/")
if response.status_code != 200:
	print('request failed')
	exit(response.status_code)
soup = bs(response.text, 'html.parser')
data = []
for item in soup.select('tr'):
	row = []
	for box in item.select('td'):
		row.append(box.text.strip())
	for box in item.select('th'):
		row.append(box.text.strip())
	data.append(row)
with open("data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)