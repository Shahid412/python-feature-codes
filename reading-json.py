import json

with open(r'person.json') as f:
	data = json.load(f)
	
print(data)  