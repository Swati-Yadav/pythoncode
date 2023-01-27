import json
with open('demo.json') as alldata:
   data = json.load(alldata)
print(data)
print(data['name'])