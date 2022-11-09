import json

f = open('assistant\queries.json')
data = json.load(f)

# for i in data['who invented battery']:
#     print(i)

res = data['who invented electric bulb']
print(res)

f.close()