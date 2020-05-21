import http.client
from json import load

from base_class import Channel

CONN = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

HEADERS = {
    "x-rapidapi-host": "free-nba.p.rapidapi.com",
    "x-rapidapi-key": "78b226d379msh5dd371b67801cd6p1f34c1jsne645d3015eea",
}


class PlayerStatsChannel(Channel):
    def __init__(self, page_size: int):
        self.page_size = page_size

    def __iter__(self):
        stats = self._get_paged_stats()
        self.page += 1
        return stats

    def __next__(self):
        stats = self._get_paged_stats()
        if len(stats) < self.page_size:
            raise StopIteration
        return stats

    def _get_paged_stats():
        CONN.request("GET", f"/stats?page={self.page}&per_page={self.page_size}", headers=HEADERS)

        res = CONN.getresponse()
        stats = _format_stats(res)
        data = load(res)
        return data
