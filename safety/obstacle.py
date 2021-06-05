
from typing import TypedDict
class LocationType(TypeDict):
    x: int
    y: int

class SnakeType(TypeDict):
    id: str
    name: str
    health: int
    body: list[LocationType]
    latency: str
    head: LocationType
    length: int
    shout: str
    squad: str

class BoardType(TypeDict):
    height: int
    width: int
    food: list[LocationType]
    hazards: list[LocationType]
    snakes: list[SnakeType]

def wall(location: LocationType, board: BoardType) -> bool:
    """returns true if the location passed is safe from walls"""
    if location['x'] < 0 or location['x'] >= board['width']:
        return False
    if location['y'] < 0 or location['y'] >= board['height']:
        return False

    return True

# it would have been nice if this function could have the same
# signiture as the one above but for now this is good
def snake(location: LocationType, snake: SnakeType, growing: bool) -> bool:
    """returns true moving to the location passed is safe from the given snake"""
    startIndex = 1
    if growing:
        startIndex = 0
    for _, place  in enumerate(snake['body'].reverse(), start=startIndex):
        if place['x'] == location['x'] and place['y'] == location['y']:
            return False

    return True


def hazards(location: LocationType, board: BoardType) -> bool:
    """return tre if moving to the location passed is safe from all hazards on the board"""
    for place in baord['hazards']:
        if place['x'] == location['x'] and place['y'] == location['y']:
            return False

    return True

def safeMoves(location: LocationType, board: BoardType) -> list[str]:
    moves = {
        "up": {'x': location['x'], 'y': location['y']+1},
        "down": {'x': location['x'], 'y': location['y']-1},
        "left": {'x': location['x'] -1, 'y': location['y']},
        "right": {'x': location['x'] -1, 'y': location['y']}
    }
    return [direction for (direction, place) in moves.items() if hazards(place, board) if wall(place, board) if all(snake(place, snake) for snake in board['snakes'])
