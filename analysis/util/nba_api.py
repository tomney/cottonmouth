import http.client

CONN = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

HEADERS = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "78b226d379msh5dd371b67801cd6p1f34c1jsne645d3015eea"
    }


def get_paged_stats(page: int, page_size: int):
    CONN.request("GET", f"/stats?page={page}&per_page={page_size}", headers=HEADERS)

    res = CONN.getresponse()
    data = res.read() 