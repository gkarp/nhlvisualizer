import json
import requests


def get_data(url):
    r = requests.get(url)
    data = r.json()
    return data


def read_json(json_data, mode='prod'):
    if mode == 'prod':
        data = json.loads(json_data)  # TO DO: inout is dict
    elif mode == 'dev':
        with open(json_data, 'r') as f:
            data = json.load(f)
    else:
        raise ValueError("Invalid input for parameter 'mode'.")
    return data


def archive_json(file):
    pass
