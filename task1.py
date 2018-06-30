import json
import requests
import requests.auth

"""Reading input from user"""
stri = raw_input('Enter String (without quotes): ')
language = raw_input('Enter Language (without quotes): ')

"""Converting curl to python requests"""
url = 'http://ws.okbqa.org:1515/templategeneration/rocknrole'
headers = {'Content-Type': 'application/json',}
data = '{\n"string": \"'+stri+'\",\n"language": \"' + language +'\"\n}'
response = requests.post(url, headers=headers, data=data)

"""Storing the json response which comes as output"""
json_data = response.json()
ans = json.dumps(json_data)

"""converting the json data to a python dictionary"""
loaded_json = json.loads(ans)

"""Parsing the response to get the desired output"""
a1 = loaded_json[0]
print 'Output: ' + a1['slots'][3]['o']
