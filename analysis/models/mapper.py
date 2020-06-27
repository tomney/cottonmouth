from typing import Dict, Tuple


def mapper(request: Dict, map: Dict) -> Dict:
    response = {}
    for key, value in map.items():
        if value is None:
            response[key] = request[key]
        else:
            response[key] = _get_nested_value(request, value)
    return response


def _get_nested_value(request: Dict, value: Tuple):
    nested_response = request
    for index in value:
        nested_response = nested_response[index]
    return nested_response
