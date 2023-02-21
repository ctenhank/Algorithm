N = int(input())
info = [list(map(int, input().split(' '))) for _ in range(N)]

GREEN, BLUE = 0, 1
dx = [1, 0]
dy = [0, 1]
mtx = [[0 for _ in range(10)] for _ in range(10)]

def create(block_info):
    t, x, y = block_info
    ret = [(x, y)]
    if t == 2: ret.append((x, y+1))
    elif t == 3: ret.append((x+1, y))
    return ret

def out_of_bound(x, y):
    if x < 0 or x > 9 or y < 0 or y > 9:
        return True
    return False

def is_cell(x, y):
    return mtx[x][y] != 0

def place(cells, color):
    # 앞 칸이 경계를 넘어섰거나 블럭이 있는경우
    is_existed = False
    while not is_existed:
        temp = []
        for x, y in cells:
            x, y = x + dx[color], y + dy[color]
            temp.append((x, y))
            if out_of_bound(x, y) or is_cell(x, y):
                is_existed = True
                break

        if not is_existed:
            cells = temp

    for x, y in cells:
        mtx[x][y] = 1

def check_green():
    ret = []
    for x in range(6, 10):
        ret.append(x)
        for y in range(4):
            if not is_cell(x, y):
                ret.pop()
                break
    return ret

def check_special_green():
    ret = 0
    for x in [4, 5]:
        for y in range(4):
            if is_cell(x, y):
                ret += 1
                break
    return ret

def push_green(x):
    temp = [[mtx[x_][y] for y in range(4)]for x_ in range(4, x)]
    for x_ in range(4, x + 1):
        for y in range(4):
            if x_ == 4:
                mtx[x_][y] = 0
            else:
                mtx[x_][y] = temp[x_-5][y]


def check_blue():
    ret = []
    for y in range(6, 10):
        ret.append(y)
        for x in range(4):
            if not is_cell(x, y):
                ret.pop()
                break
    return ret

def check_special_blue():
    ret = 0
    for y in [4, 5]:
        for x in range(4):
            if is_cell(x, y):
                ret += 1
                break
    return ret

def push_blue(y):
    temp = [[mtx[x][y_] for y_ in range(4, y)]for x in range(4)]
    for y_ in range(4, y + 1):
        for x in range(4):
            if y_ == 4:
                mtx[x][y_] = 0
            else:
                mtx[x][y_] = temp[x][y_ - 5]

def print_blocks():
    print('-' * 10)
    for i in range(10):
        for j in range(10):
            if i > 3 and j > 3:
                continue
            print(mtx[i][j], end=' ')
        print()

def remains():
    ret = 0
    for i in range(10):
        for j in range(10):
            if i < 4 and j < 4: continue
            if i > 4 and j > 4: continue

            if mtx[i][j] > 0:
                ret += mtx[i][j]
    return ret

ans = 0 
for block in info:
    cells = create(block)
    # green
    place(cells, GREEN)
    indices = sorted(check_green())
    for index in indices:
        ans += 1
        push_green(index)

    specials = check_special_green()
    for _ in range(specials):
        push_green(9)

    # blue
    place(cells, BLUE)
    indices = sorted(check_blue())
    for index in indices:
        ans += 1
        push_blue(index)

    specials = check_special_blue()
    for _ in range(specials):
        push_blue(9)

print(ans)
print(remains())