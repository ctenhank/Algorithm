import sys

current = sys.stdin.readline().rstrip()

# 앞에 나온 방향으로 2칸 간 뒤 나머지 한 칸으로 간다.
# LU, LD, RU, RD, UL, UR, DL, DR
dr = [-1, 1, -1, 1, -2, -2, 2, 2]
dc = [-2, -2, 2, 2, -1, 1, -1, 1]


def out_of_garden(cur, idx):
    r, c = cur
    if r + dr[idx] < 1 or r + dr[idx] > 8 or c + dc[idx] < 1 or c + dc[idx] > 8:
        return True
    return False


c, r = current[0:1], current[1:2]
r, c = int(r), ord(c) - ord("a") + 1

current = (r, c)
ret = 0
for i in range(8):
    if out_of_garden(current, i):
        continue
    ret += 1
print(ret)
