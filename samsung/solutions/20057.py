# 여기서 알아낸 것
# 매트릭스 90도 회전, 중심으로부터 회전

N = int(input())
mtx = [list(map(int, input().split(' '))) for _ in range(N)]

skill_range = 5
skill = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 'alpha', 'y', 'x', 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0],
]

# 토네이도 셀단위 이동
EAST, NORTH, WEST, SOUTH = 0, 1, 2, 3
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

visited = [[False for _ in range(N)]for _ in range(N)]

# 중요한 점
# 1. 토네이도: 매트릭스 중점으로부터 반시계방향으로 (1, 1)
#  - 토네이도는 무조건 좌측 90도 회전만 수행
#    -> 매번 좌측 90도 회전을 수행했을 때의 칸이 이미 방문했으면 앞으로 가면 됨
# 2. 방향마다 바뀌는 dx, dy, 모래 값 sand_dx, sand_dy를 잘 활용하는 법이 무엇일까?
def rotate():
    global skill
    center = (int(skill_range/2), int(skill_range/2))
    ret = [[0 for _ in range(skill_range)]for _ in range(skill_range)]
    for r in range(skill_range):
        for c in range(skill_range):
            diff = (r - center[0], c - center[1])
            rotated = (center[0] - diff[1], center[1] - (-diff[0]))
            ret[rotated[0]][rotated[1]] = skill[r][c]
    skill = ret
    return skill

skills = {
    WEST: skill,
    SOUTH: rotate(),
    EAST: rotate(),
    NORTH: rotate(),
}


def turn_left_90_degree(current_direction):
    return (current_direction + 1) % 4


def out_of_bound(loc):
    if loc[0] < 0 or loc[0] > N-1 or loc[1] < 0 or loc[1] > N-1:
        return True
    return False

# x   : 현재 위치 
# cur : 방향
def blow(x, cur):
    y = (x[0] + dr[cur], x[1] + dc[cur])

    # x에서부터 y로 옮겨짐
    mtx[y[0]][y[1]] += mtx[x[0]][x[1]]
    mtx[x[0]][x[1]] = 0

    # 변수 재명명
    total_sand = mtx[y[0]][y[1]]
    left = mtx[y[0]][y[1]]
    ret = 0
    
    # y가 정중앙
    for r in range(skill_range):
        for c in range(skill_range):
            if skills[cur][r][c] in [ 'alpha', 'y', 'x'] or\
                skills[cur][r][c] == 0:
                continue

            dx, dy = r - 2, c - 2
            _sand = int(skills[cur][r][c] * total_sand)
            loc = (y[0] + dx, y[1] + dy)
            if not out_of_bound(loc):
                mtx[loc[0]][loc[1]] +=  _sand
            else:
                ret += _sand
            left -= _sand

    mtx[y[0]][y[1]] = 0
    alpha = (y[0] + dr[cur], y[1] + dc[cur])

    if not out_of_bound(alpha):
        mtx[alpha[0]][alpha[1]] += left
    else:
        ret += left

    return ret

def tornado():
    ans = 0
    x = (int(N/2), int(N/2))
    cur = NORTH

    while True:
        visited[x[0]][x[1]] = True
        if x == (0, 0):
            break

        next = turn_left_90_degree(cur)
        if not visited[x[0] + dr[next]][x[1] + dc[next]]:
            cur = next
        
        ans += blow(x, cur)
        x = (x[0] + dr[cur], x[1] + dc[cur])

    return ans

print(tornado())
