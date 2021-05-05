import requests


def get_player_game_stats(count):
    page_size = 100
    params = {
        "seasons": [2020],
        "per_page": int(count*page_size),
        "page": count,
    }
    response = requests.get("https://www.balldontlie.io/api/v1/stats", params)
    return response

def write_stats_to_csv(stats):
    return ""

def write_file_to_cloud(filename):
    return ""

def append_cloud_file_to_bigquery_table(cloud_file, identifier, table_name):
    pass

def process():
    done = False
    count = 0
    while not done:
        get_player_game_stats(count)
        filename = write_stats_to_csv(stats)
        cloud_file = write_file_to_cloud(filename)
        append_cloud_file_to_bigquery_table(cloud_file, player, "player_stats")
        count += count

process()