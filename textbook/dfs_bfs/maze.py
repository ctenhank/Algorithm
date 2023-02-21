import sys
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

MONSTER = 0
NON_MONSTER = 1


def split_by_a_character(txt: str):
    ret = []
    for i in range(len(txt)):
        ret.append(txt[i : i + 1])
    return ret


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [
    list(map(int, split_by_a_character(sys.stdin.readline().rstrip())))
    for _ in range(N)
]


def out_of_bound(location):
    r, c = location
    if r < 0 or r > N - 1 or c < 0 or c > M - 1:
        return True
    return False


def bfs(maze, start, end):
    visited = [[False for _ in range(M)] for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if maze[r][c] == MONSTER:
                visited[r][c] = True

    distance = [[sys.maxsize for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if out_of_bound((nr, nc)):
                continue

            if not visited[nr][nc]:
                visited[nr][nc] = True
                distance[nr][nc] = min(distance[r][c] + 1, distance[nr][nc])
                queue.append((nr, nc))

    return distance[end[0]][end[1]]


print(bfs(maze, (0, 0), (N - 1, M - 1)))
