from typing import TypedDict


class Player(TypedDict):
    id: int
    first_name: str
    height_feet: int
    height_inches: int
    last_name: str
    # TODO: make this an enum
    position: str
    team_id: int
    weight_pounds: int


class PlayerRepo(TypedDict):
    external_id: int
    first_name: str
    height_feet: int
    height_inches: int
    last_name: str
    # TODO: make this an enum
    position: str
    external_team_id: int
    weight_pounds: int
