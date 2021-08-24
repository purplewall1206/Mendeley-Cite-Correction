from scholarly import scholarly
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

print(titles[0])
search_query = scholarly.search_pubs(titles[0])
scholarly.pprint(next(search_query))
# paper = scholarly.fill(next(search_query))
# print(paper)
# for t in titles:
#     print(t)
# search_query = scholarly.search_author('Steven A Cholewiak')
# author = scholarly.fill(next(search_query))
# print(author)
# print([pub['bib']['title'] for pub in author['publications']])

# Take a closer look at the first publication
# pub = scholarly.fill(author['publications'][0])
# print(pub)

# Which papers cited that publication?
# print([citation['bib']['title'] for citation in scholarly.citedby(pub)])