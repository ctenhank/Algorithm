import sys

sys.setrecursionlimit(10**6)

def solve(n, num_bag):
    if n < 0: return sys.maxsize
    if n == 0: return num_bag

    ret = sys.maxsize
    if n >= 5: ret = min(ret, solve(n - 5, num_bag + 1))
    if ret == sys.maxsize: ret = min(ret, solve(n - 3, num_bag + 1))

    return ret

n = int(input())
ans = solve(n, 0)
if ans == sys.maxsize:
    ans = -1
print(ans)