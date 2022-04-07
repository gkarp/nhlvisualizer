import argparse
import json
import requests


def get_standings(url):
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


def parse_standings(data):
    pass


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('mode',
                        help='If prod: hit api, if dev:'
                             'hit saved copy of json.',
                        choices=['dev', 'prod'])

    args = parser.parse_args()
    mode = args.mode
    standings_url = "https://statsapi.web.nhl.com/api/v1/standings"
    if mode == 'prod':
        source_data = get_standings(standings_url)
    else:
        source_data = 'src/nhlvisual/data/standings.json'
    loaded_data = read_json(source_data, mode=mode)['records']
    print(type(loaded_data))


if __name__ == "__main__":
    main()
