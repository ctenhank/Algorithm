import sys

HOLE = 0
WALL = 1

# 상하좌우 순
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def split_by_a_characher(txt: str):
    ret = []
    for i in range(len(txt)):
        ret.append(txt[i : i + 1])
    return ret


def out_of_bound(location):
    global N
    global M
    r, c = location
    if r < 0 or r > N - 1 or c < 0 or c > M - 1:
        return True
    return False


def dfs(graph, current, visited):
    r, c = current
    visited[r][c] = True

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not out_of_bound((nr, nc)) and not visited[nr][nc]:
            dfs(graph, (nr, nc), visited)


def ice_cream(graph):
    num = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if graph[r][c] == WALL:
                visited[r][c] = True

    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                dfs(graph, (r, c), visited)
                num += 1

    return num


N, M = map(int, sys.stdin.readline().rstrip().split())
frame = [
    list(map(int, split_by_a_characher(sys.stdin.readline().rstrip())))
    for _ in range(N)
]
print(ice_cream(frame))
