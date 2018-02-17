import json
json_data = open('/home/user/git/nlp/text/test.json').read()
data = json.loads(json_data)
print(data)
