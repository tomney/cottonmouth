from typing import TypedDict

from game import Game
from player import Player
from team import Team


class PlayerGame(TypedDict):
    external_id: int
    ast: int
    blk: int
    dreb: int
    fg3_pct: float
    fg3a: int
    fg3m: int
    fg_pct: float
    fga: int
    fgm: int
    ft_pct: float
    fta: int
    ftm: int
    game: Game
    min: str
    oreb: int
    pf: int
    player: Player
    pts: int
    reb: int
    stl: int
    team: Team
    turnover: int


class PlayerGameRepo(TypedDict):
    external_team_id: int
    team_name: str
    external_game_id: int
    ast: int
    turnover: int
    blk: int
    stl: int
    dreb: int
    oreb: int
    fg3a: int
    fg3m: int
    # fga includes fg3a
    fga: int
    # fgm includes fg3m
    fgm: int
    fta: int
    ftm: int
    min: str
    pf: int
    height_inches: int
    # TODO use enum
    position: str
    game_date: str
