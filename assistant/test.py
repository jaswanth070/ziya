import json
import csv


def json_search(query):
    a = open('assistant\queries.json')
    b = open('assistant\capital.json')
    data_a = json.load(a)
    # data_a = json.load(b)
    try:
        res = data_a.keys()
        # print(res)

        for i in res:
            if query in i:
                return (data_a[i])
            # print(i)
        # print(data)
        a.close()
    except:
        return False

print(json_search('introvert'))

