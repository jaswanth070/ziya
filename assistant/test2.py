import json

query = input()


b = open('assistant\capital.json')
data = json.load(b)
query = query.lower()
for i in data:
    if query == i['country'].lower():
        print(i['capital'])
