
from typing import TypedDict, List
class LocationType(TypedDict):
    x: int
    y: int

class SnakeType(TypedDict):
    id: str
    name: str
    health: int
    body: List[LocationType]
    latency: str
    head: LocationType
    length: int
    shout: str
    squad: str

class BoardType(TypedDict):
    height: int
    width: int
    food: List[LocationType]
    hazards: List[LocationType]
    snakes: List[SnakeType]

obsticleString = "just some value"
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
    rbody = snake['body']
    rbody.reverse()
    for _, place  in enumerate(rbody, start=startIndex):
        if place['x'] == location['x'] and place['y'] == location['y']:
            return False

    return True


def hazards(location: LocationType, board: BoardType) -> bool:
    """return tre if moving to the location passed is safe from all hazards on the board"""
    for place in board['hazards']:
        if place['x'] == location['x'] and place['y'] == location['y']:
            return False

    return True

def safeMoves(location: LocationType, board: BoardType) -> List[str]:
    moves = {
        "up": {'x': location['x'], 'y': location['y']+1},
        "down": {'x': location['x'], 'y': location['y']-1},
        "left": {'x': location['x'] -1, 'y': location['y']},
        "right": {'x': location['x'] +1, 'y': location['y']}
    }
    return [direction for (direction, place) in moves.items() if hazards(place, board) if wall(place, board) if all(snake(place, worm, False) for worm in board['snakes'])]
