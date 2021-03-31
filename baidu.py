import requests 
import base64
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5zaywXOKVa6aVLaDclbkvxrb&client_secret=K1uZU3QYu7LorPGXNIIzmtrsH8tkYBwb'
response = requests.get(host)
if response:
    access_token=response.json()['access_token']
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
f = open('./imgs/0.png', 'rb')
img = base64.b64encode(f.read())
params = {"image":img,'detect_direction':'true'}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    for i in response.json()['words_result']:
        print(i['words'])