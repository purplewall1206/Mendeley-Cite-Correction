import requests
import os


os.environ["http_proxy"] = "http://127.0.0.1:20171"
os.environ["https_proxy"] = "http://127.0.0.1:20171"

titles = []

with open('title.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        i = line.find('}}')
        x = line[10:i]
        titles.append(x)

test = 'eternal memory war'
print(test)
payload = {'q' : test, 'format' : 'json', 'h':'1'}
r = requests.get('https://dblp.org/search/publ/api', params=payload)
print(r.text)