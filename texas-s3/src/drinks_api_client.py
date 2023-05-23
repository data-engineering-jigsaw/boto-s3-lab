import json
import boto3
import requests

name = 'HONDURAS MAYA CAFE & BAR LLC'
url = "https://data.texas.gov/resource/naix-2893.json"
response = requests.get(url, params = {'taxpayer_name': name})

def write_to_json(data, rest_name):
    pass



def read_from_file(rest_name):
    pass

