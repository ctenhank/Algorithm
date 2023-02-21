dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N,M,K = list(map(int, input().split(' ')))
grid = [[[] for _ in range(N)] for _ in range(N)]
fireballs = [list(map(int, input().split(' '))) for _ in range(M)]

class Fireball:
    def __init__(self, m, s, d):
        self.m = m
        self.s = s
        self.d = d

def is_every_odd_or_even(directions):
    vals = list(map(lambda e: e%2, directions))
    return len(set(vals)) == 1

def move(fireballs):
    ret = []
    for fireball in fireballs:
        r, c, m, s, d  = fireball
        r = (r + s * dr[d]) % N
        c = (c + s * dc[d]) % N
        ret.append([r, c, m, s, d])
    return ret

def event(fireballs):
    ret = []
    grid = {}
    for fireball in fireballs:
        r, c, m, s, d = fireball
        if (r, c) not in grid:
            grid[(r, c)] = []
        grid[(r, c)].append([m, s, d])

    for key in grid:
        r, c = key
        items = grid[(r, c)]
        if len(items) >= 2:
            m, s, d = 0, 0, []
            for fireball in items:
                m += fireball[0]
                s += fireball[1]
                d.append(fireball[2])

            m = int(m / 5)
            s = int(s / len(items))
            if m > 0:
                next = [1, 3, 5, 7]
                if is_every_odd_or_even(d):
                    next = [0, 2, 4, 6]

                for i in range(4):
                    ret.append([r, c, m, s, next[i]])
        else: 
            ret.append([r, c, items[0][0], items[0][1], items[0][2]])

    return ret

for _ in range(K):
    moved = move(fireballs)
    fireballs = event(moved)

ans = 0
for fireball in fireballs:
    ans += fireball[2]
print(ans)