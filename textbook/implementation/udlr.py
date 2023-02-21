import sys

N = int(sys.stdin.readline().rstrip())
plan = sys.stdin.readline().rstrip().split()

# L, R, U, D 순
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
way_to_index = {"L": 0, "R": 1, "U": 2, "D": 3}


def out_of_map(current, next):
    r, c = current
    if r + dr[next] < 1 or r + dr[next] > N or c + dc[next] < 1 or c + dc[next] > N:
        return True
    return False


# starting point
sp = (1, 1)
for way in plan:
    idx = way_to_index[way]
    if not out_of_map(sp, idx):
        r = sp[0] + dr[idx]
        c = sp[1] + dc[idx]
        sp = (r, c)

print(sp[0], sp[1])
