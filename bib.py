import requests
import os
import json
import time

# os.environ["http_proxy"] = "http://127.0.0.1:20171"
# os.environ["https_proxy"] = "http://127.0.0.1:20171"

titles = []
ext = []

title_set = set() # remove dups

with open('title.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        i = line.find('}}')
        x = line[10:i]
        title_set.add(x)
        # titles.append(x)

print(len(title_set))
titles = list(title_set)

bibtex = []

for title in titles:
    payload = {'q' : title, 'format' : 'json', 'h' : '1'}
    r = requests.get('https://dblp.org/search/publ/api', params=payload)
    jsondata = json.loads(r.text)
    try:
        key = jsondata['result']['hits']['hit'][0]['info']['key']
        url = 'https://dblp.org/rec/' + key + '.bib'
        time.sleep(2)
        print(url)
        r1 = requests.get(url)
        bibtex.append(r1.text)
    except:
        ext.append(title)

with open('ref.bib', 'w') as f:
    for b in bibtex:
        f.write(b)
        print(b)

# test = 'eternal memory war'
# print(test)
# payload = {'q' : test, 'format' : 'json', 'h':'1'}
# r = requests.get('https://dblp.org/search/publ/api', params=payload)
# # print(r.text)

# # json_str = json.dumps(r.text)
# new_dict = json.loads(r.text)

# key = (new_dict['result']['hits']['hit'][0]['info']['key'])
# url = 'https://dblp.org/rec/'

# r1 = requests.get(url + key + '.bib')

# print(type(dict))

# @article{DBLP:journals/ieeesp/SzekeresPWS14,
#   author    = {Laszlo Szekeres and
#                Mathias Payer and
#                Tao Wei and
#                R. Sekar},
#   title     = {Eternal War in Memory},
#   journal   = {{IEEE} Secur. Priv.},
#   volume    = {12},
#   number    = {3},
#   pages     = {45--53},
#   year      = {2014},
#   url       = {https://doi.org/10.1109/MSP.2014.44},
#   doi       = {10.1109/MSP.2014.44},
#   timestamp = {Sun, 15 Mar 2020 19:46:22 +0100},
#   biburl    = {https://dblp.org/rec/journals/ieeesp/SzekeresPWS14.bib},
#   bibsource = {dblp computer science bibliography, https://dblp.org}
# }

# class bibtex:
#     author = ""
#     title  = ""
#     journal = ""
#     volume = ""
#     number = ""
#     pages = ""
#     year = ""
#     url = ""
#     doi = ""
#     timestamp = ""