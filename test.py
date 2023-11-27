import json

with open('./data.json') as f:
    json_data = f.read()

print(json_data)