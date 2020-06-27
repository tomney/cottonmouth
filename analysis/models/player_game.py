from typing import TypedDict

from models.game import Game
from models.player import Player
from models.team import Team


PlayerGameMap = {
    "id": None,
    "ast": None,
    "blk": None,
    "dreb": None,
    "fg3_pct": None,
    "fg3a": None,
    "fg3m": None,
    "fg_pct": None,
    "fga": None,
    "fgm": None,
    "ft_pct": None,
    "fta": None,
    "ftm": None,
    "min": None,
    "oreb": None,
    "pf": None,
    "pts": None,
    "reb": None,
    "stl": None,
    "turnover": None,
    "team": ("team", "id"),
    "player": ("player", "id"),
    "game": ("game", "id"),
}


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
