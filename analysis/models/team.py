from typing import TypedDict


class Team(TypedDict):
    id: int
    abbreviation: str
    city: str
    conference: str
    division: str
    full_name: str
    name: str


class TeamRepo(TypedDict):
    external_id: int
    abbreviation: str
    city: str
    conference: str
    division: str
    full_name: str
    name: str
