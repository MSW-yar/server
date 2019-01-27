import requests
from bson.json_util import loads

IP = 'http://localhost:8000/'


def get():
    response = requests.get(IP)
    # res = loads(response)
    print(response.json())

    # print(response.json())
    # response=response.json()
    # print (response['overview'])
    # return response['overview']

def post(body):
    data = {'body': body}
    response = requests.post(IP + 'post', data)
    response=response.json()
    # return response.text


