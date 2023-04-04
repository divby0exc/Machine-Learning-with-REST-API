
import requests
import json

url_ann = 'http://127.0.0.1:5000/get_ml_pred'
url_ml = 'http://127.0.0.1:5000/get_ann_pred'

input = [[5.6, 	0.85, 	0.05, 	1.4, 	0.045, 	12.0, 	88.0, 	0.9924, 	3.56, 	0.82, 	12.9]]
j_data = json.dumps(input)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
# r = requests.post(url_ann, data=j_data, headers=headers)
s = requests.post(url_ml, data=j_data, headers=headers)
# print(r, r.text)
print(s, s.text)
