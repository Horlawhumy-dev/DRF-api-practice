from django.test import TestCase
import requests, json

response = requests.get('http://127.0.0.1:8000/api/task-list/')
json_res = json.loads(response.text)
# print(json_res)
assert len(json_res) >= 5

data = {"title": "owner", "owner": "title", "completed":True}
res = requests.put('http://127.0.0.1:8000/api/task-update/42', data)
res_json = json.loads(res.content)
# print(res_json)
# requests.post('http://127.0.0.1:8000/api/task-create/', data)
# print(json_res)
