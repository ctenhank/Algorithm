import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
map_ = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

LAND = 0
SEA = 1

# N, E, S, W 방향 순서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

current = r, c
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if map_[i][j] == SEA:
            visited[i][j] = True


def out_of_map(current, idx):
    r, c = current
    if r + dr[idx] < 0 or r + dr[idx] > N - 1 or c + dc[idx] < 0 or c + dc[idx] > M - 1:
        return True
    return False


def turn_left(d):
    return (d - 1) % 4


ret = 0
while True:
    # 방향 변경
    d = turn_left(d)
    if out_of_map(current, d):
        continue

    r, c = current
    if not visited[r + dr[d]][c + dc[d]]:
        current = (r + dr[d], c + dc[d])
        visited[current[0]][current[1]] = True
        ret += 1
    else:
        no_way = True
        for i in range(3):
            d = turn_left(d)
            if not visited[r + dr[d]][c + dc[d]]:
                no_way = False

        if no_way:
            oppsite = turn_left(turn_left(d))
            if (
                out_of_map(current, oppsite)
                or map_[r + dr[oppsite]][c + dc[oppsite]] == SEA
            ):
                break
            else:
                current = (r + dr[oppsite], c + dc[oppsite])
        else:
            d = turn_left(d)


print(ret)
