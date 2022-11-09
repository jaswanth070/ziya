import json


f = open('assistant\queries.json')
data = json.load(f)

query = input()

try:
# for i in data['who invented battery']:
#     print(i)
    res = data.keys()
    # print(res)

    for i in res:
        if query in i:
            print(data[i])
            break
        # print(i)
    # print(data)
    f.close()
except:
    print("No results found")