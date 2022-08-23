import argparse

from constants import STANDINGS_URL
from common import get_data, read_json


def parse_standings(team_data):
    row = dict()
    row['id'] = team_data['team']['id']
    row['name'] = team_data['team']['name']
    row['gp'] = team_data['gamesPlayed']
    row['wins'] = team_data['leagueRecord']['wins']
    row['losses'] = team_data['leagueRecord']['losses']
    row['ot'] = team_data['leagueRecord']['ot']
    row['pt_pcg'] = team_data['pointsPercentage']
    return row


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('mode',
                        help='If prod: hit api, if dev:'
                             'hit saved copy of json.',
                        choices=['dev', 'prod'])

    args = parser.parse_args()
    mode = args.mode

    if mode == 'prod':
        source_data = get_data(STANDINGS_URL)
    else:
        source_data = 'src/nhlvisual/data/standings.json'
    loaded_data = read_json(source_data, mode=mode)['records']

    records = []
    for division in loaded_data:
        for t in division['teamRecords']:
            record = parse_standings(t)
            records.append(record)


if __name__ == "__main__":
    main()
