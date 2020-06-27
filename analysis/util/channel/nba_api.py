import http.client
from json import load
from typing import List

from util.channel.base_class import Channel
from models.mapper import mapper
from models.player_game import PlayerGameMap


CONN = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

HEADERS = {
    "x-rapidapi-host": "free-nba.p.rapidapi.com",
    "x-rapidapi-key": "78b226d379msh5dd371b67801cd6p1f34c1jsne645d3015eea",
}


class PlayerStatsChannel(Channel):
    def __init__(self, page_size: int, page_limit: int = -1):
        self.page_size = page_size
        self.page = 1
        self.page_limit = page_limit

    def __iter__(self):
        self.stats = self.read()
        return self

    def __next__(self):
        if self.page == self.page_limit:
            raise StopIteration
        stats = self.read()
        if len(stats) < self.page_size:
            raise StopIteration
        self.page = self.page + 1
        return stats

    def read(self):
        CONN.request(
                "GET",
                f"/stats?page={self.page}&per_page={self.page_size}",
                headers=HEADERS
            )

        json_res = CONN.getresponse()
        res = load(json_res)
        formatted_data = self.format_data(res)
        return formatted_data

    @staticmethod
    def format_data(data: dict) -> List[dict]:
        raw_player_games = data['data']
        player_games = []
        for raw_player_game in raw_player_games:
            player_game = mapper(raw_player_game, PlayerGameMap)
            player_games.append(player_game)
        return player_games
