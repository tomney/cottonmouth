import requests


def get_player_game_stats(count):
    page_size = 10
    # headers = {
    #     "x-rapidapi-host": "free-nba.p.rapidapi.com",
    #     "x-rapidapi-key": "78b226d379msh5dd371b67801cd6p1f34c1jsne645d3015eea",
    # }
    params = {
        "seasons": [2020],
        "per_page": int(page_size),
        "page": count,
    }
    response = requests.get("https://www.balldontlie.io/api/v1/stats", params)
    # response = requests.get("https://free-nba.p.rapidapi.com/stats?page={count}&per_page={page_size}", params=params, headers=headers)
    return response, len(response)<page_size

def write_stats_to_csv(stats):
    return ""

def write_file_to_cloud(filename):
    return ""

def append_cloud_file_to_bigquery_table(cloud_file, identifier, table_name):
    pass

def flattenDict(d, result=None):
    """
    https://gist.github.com/higarmi/6708779
    """
    if result is None:
        result = {}
    for key in d:
        value = d[key]
        if isinstance(value, dict):
            value1 = {}
            for keyIn in value:
                value1[".".join([key,keyIn])]=value[keyIn]
            flattenDict(value1, result)
        elif isinstance(value, (list, tuple)):
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    index = 0
                    for keyIn in element:
                        newkey = ".".join([key,keyIn])
                        value1[".".join([key,keyIn])]=value[indexB][keyIn]
                        index += 1
                    for keyA in value1:
                        flattenDict(value1, result)
        else:
            result[key]=value
    return result

def process():
    done = False
    count = 0
    while not done:
        player_game_stats, more = get_player_game_stats(count)
        if not more:
            done = true
        flattened_stats = []
        for stat in stats:
            flattened_stat = flattenDict(stat)
            flattened_stats.append(flattened_stat)
        filename = write_stats_to_csv(flattened_stats)
        cloud_file = write_file_to_cloud(filename)
        append_cloud_file_to_bigquery_table(cloud_file, player, "player_stats")
        count += count

process()