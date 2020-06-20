from typing import TypedDict


class Game(TypedDict):
    external_id: int
    date: str
    external_home_team_id: int
    home_team_score: int
    period: int
    postseason: bool
    season: int
    # TODO: make enum
    status: str
    time: str
    external_visitor_team_id: int
    visitor_team_score: int


class GameRepo(TypedDict):
    external_id: int
    date: str
    home_team_id: int
    home_team_score: int
    period: int
    postseason: bool
    season: int
    status: str
    time: str
    visitor_team_id: int
    visitor_team_score: int
