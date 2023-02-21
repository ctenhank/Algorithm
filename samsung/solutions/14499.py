
N, M, x, y, K = list(map(int, input().split(' ')))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
orders = list(map(int, input().split(' ')))
EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
TOP, BOTTOM = 0, 5
dice = [0 for _ in range(6)]

dx = [99, 0,  0, -1, 1]
dy = [99, 1, -1,  0, 0]

def out_of_bound(loc):
    if loc[0] < 0 or loc[0] > N - 1 or loc[1] < 0 or loc[1] > M -1:
        return True
    return False

def east():
    _dice = [0 for _ in range(6)]
    _dice[TOP] = dice[WEST]
    _dice[BOTTOM] = dice[EAST]

    _dice[EAST] = dice[TOP]
    _dice[WEST] = dice[BOTTOM]

    _dice[NORTH] = dice[NORTH]
    _dice[SOUTH] = dice[SOUTH]
    return _dice

def west():
    _dice = [0 for _ in range(6)]
    _dice[TOP] = dice[EAST]
    _dice[BOTTOM] = dice[WEST]

    _dice[WEST] = dice[TOP]
    _dice[EAST] = dice[BOTTOM]

    _dice[NORTH] = dice[NORTH]
    _dice[SOUTH] = dice[SOUTH]
    return _dice

def north():
    _dice = [0 for _ in range(6)]
    _dice[TOP] = dice[SOUTH]
    _dice[BOTTOM] = dice[NORTH]

    _dice[NORTH] = dice[TOP]
    _dice[SOUTH] = dice[BOTTOM]

    _dice[WEST] = dice[WEST]
    _dice[EAST] = dice[EAST]
    return _dice

def south():
    _dice = [0 for _ in range(6)]
    _dice[TOP] = dice[NORTH]
    _dice[BOTTOM] = dice[SOUTH]

    _dice[NORTH] = dice[BOTTOM]
    _dice[SOUTH] = dice[TOP]

    _dice[WEST] = dice[WEST]
    _dice[EAST] = dice[EAST]
    return _dice


def get_value(cur):
    return maps[cur[0]][cur[1]]
def set_value(cur, value):
    maps[cur[0]][cur[1]] = value

cur = (x, y)
for direction in orders:
    next = (cur[0] + dx[direction], cur[1] + dy[direction])
    if out_of_bound(next):
        continue

    if direction == EAST:
        dice = east()
    elif direction == WEST:
        dice = west()
    elif direction == NORTH:
        dice = north()
    else:
        dice = south()

    print(dice[TOP])
    val = get_value(next)
    if val == 0:
        set_value(next, dice[BOTTOM])
    else:
        dice[BOTTOM] = val
        set_value(next, 0)

    cur = next

        



