import http.client
from json import load
from typing import List

from util.channel.base_class import Channel


CONN = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

HEADERS = {
    "x-rapidapi-host": "free-nba.p.rapidapi.com",
    "x-rapidapi-key": "78b226d379msh5dd371b67801cd6p1f34c1jsne645d3015eea",
}


class PlayerStatsChannel(Channel):
    def __init__(self, page_size: int):
        self.page_size = page_size
        self.page = 1

    def __iter__(self):
        self.stats = self.read()
        return self

    def __next__(self):
        stats = self.read()
        if len(stats) < self.page_size:
            raise StopIteration
        self.page = self.page + 1
        return stats

    def read(self):
        print(self.page)
        CONN.request(
                "GET",
                f"/stats?page={self.page}&per_page={self.page_size}",
                headers=HEADERS
            )

        res = CONN.getresponse()
        data = load(res)['data']
        return data

    @staticmethod
    def format_data(data: dict) -> List[dict]:
        raw_player_games = data['data']
        player_games = []
        for raw_player_game in raw_player_games:
            player_game = {
                "external_id": raw_player_game["id"],
                "ast": raw_player_game["ast"],
                "blk": raw_player_game["blk"],
                "dreb": raw_player_game["dreb"],
                "fg3_pct": raw_player_game["fg3_pct"],
                "fg3a": raw_player_game["fg3a"],
                "fg3m": raw_player_game["fg3m"],
                "fg_pct": raw_player_game["fg_pct"],
                "fga": raw_player_game["fga"],
                "fgm": raw_player_game["fgm"],
                "ft_pct": raw_player_game["ft_pct"],
                "fta": raw_player_game["fta"],
                "ftm": raw_player_game["ftm"],
                "min": raw_player_game["min"],
                "oreb": raw_player_game["oreb"],
                "pf": raw_player_game["pf"],
                "pts": raw_player_game["pts"],
                "reb": raw_player_game["reb"],
                "stl": raw_player_game["stl"],
                "turnover": raw_player_game["turnover"],
                "team": raw_player_game["team"]["id"],
                "player": raw_player_game["player"]["id"],
                "game": raw_player_game["game"]["id"],
            }
            player_games.append(player_game)
        return player_games
