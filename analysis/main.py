import requests
import json
import collections
import common.auth as auth
import pandas as pd

SCHEMA = {
    "id": str,
    "ast": str,
    "blk": str,
    "dreb": str,
    "fg3a": str,
    "fg3m": str,
    "fga": str,
    "fgm": str,
    "fta": str,
    "ftm": str,
    "game_id": str,
    "game_date": str,
    "game_home_team_id": str,
    "game_home_team_score": str,
    "game_period": str,
    "game_postseason": str,
    "game_season": str,
    "game_status": str,
    "game_time": str,
    "game_visitor_team_id": str,
    "game_visitor_team_score": str,
    "min": str,
    "oreb": str,
    "pf": str,
    "player_id": str,
    "player_first_name": str,
    "player_height_feet": str,
    "player_height_inches": str,
    "player_last_name": str,
    "player_position": str,
    "player_team_id": str,
    "player_weight_pounds": str,
    "pts": str,
    "reb": str,
    "stl": str,
    "team_id": str,
    "team_abbreviation": str,
    "team_city": str,
    "team_conference": str,
    "team_division": str,
    "team_full_name": str,
    "team_name": str,
    "turnover": str,
}

def get_player_game_stats(count):
    done=False
    page_size = 100
    params = {
        "seasons": [2020],
        "per_page": int(page_size),
        "page": count,
    }
    response = requests.get("https://www.balldontlie.io/api/v1/stats", params)
    if response.ok != True:
        error = response.text
        raise Exception(f'Invalid response: {error}')
    body = json.loads(response.text)
    current_page = body['meta']['current_page']
    # print(f'Got page:{current_page}')
    player = body['data'][0]['player']['last_name']
    game_id = body['data'][0]['id']
    print(f'Adding {player}')
    print(f'Game ID: {game_id}')
    if body['meta']['total_pages'] == current_page+1:
        done = True
    schema_rows = []
    for row in body['data']:
        flat_row = flatten_row(row)
        schema_row = force_to_schema(flat_row)
        schema_rows.append(schema_row)
    return schema_rows, done

def force_to_schema(row):
    schema_row = {}
    for field in SCHEMA.keys():
        raw_value=row.get(field)
        schema_row[field]=SCHEMA[field](raw_value)
        # It looks like types can be wrong too, set the type and use a proper null value
    return schema_row

def flatten_row(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten_row(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def process():
    creds = auth.get_credentials()
    done = False
    count = 11253
    # count = 10351
    while not done:
        stats, done = get_player_game_stats(count)
        df = pd.DataFrame(stats)
        df.to_gbq(destination_table="cell_the_team.player_game", project_id="bolg-229922", if_exists="append", credentials=creds)
        count = count + 1
        print(f'count: {count}')

process()