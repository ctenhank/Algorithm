# delta row, delta column
W, NW, N, NE, E, SE, S, SW = 1, 2, 3, 4, 5, 6, 7, 8
dr = [-1, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0, -1]

size, skill_count = list(map(int, input().split(' ')))
board = [list(map(int, input().split(' '))) for _ in range(size)]
skills = [list(map(int, input().split(' '))) for _ in range(skill_count)]
cloud = [(size-1, 0), (size-1, 1), (size-2, 0), (size-2, 1)]

def out_of_bound(loc):
    return loc[0] < 0 or loc[0] > size - 1 or loc[1] < 0 or loc[1] > size - 1


def exists_water(loc):
    if not out_of_bound(loc) and board[loc[0]][loc[1]] > 0:
        return True
    return False


def copy_water(cloud):
    for r, c in cloud:
        disappeared[r][c] = True
        if exists_water((r + dr[NW], c + dc[NW])):
            board[r][c] += 1
        if exists_water((r + dr[NE], c + dc[NE])):
            board[r][c] += 1
        if exists_water((r + dr[SW], c + dc[SW])):
            board[r][c] += 1
        if exists_water((r + dr[SE], c + dc[SE])):
            board[r][c] += 1


def move(cloud, direction, step):
    ret = []
    for _cloud in cloud:
        r = (_cloud[0] + step * dr[direction]) % size
        c = (_cloud[1] + step * dc[direction]) % size
        ret.append((r, c))
        board[r][c] += 1
    return ret


def generate():
    ret = []
    for r in range(size):
        for c in range(size):
            if board[r][c] >= 2 and not disappeared[r][c]:
                board[r][c] -= 2
                ret.append((r, c))
    return ret


for skill in skills:
    disappeared = [[False for _ in range(size)] for _ in range(size)]    
    d, s = skill
    copy_water(move(cloud, d, s))
    cloud = generate()

ans = 0
for r in range(size):
    for c in range(size):
        ans += board[r][c]
print(ans)
