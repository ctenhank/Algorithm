import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
first, second = 0, 0

# 나누어 떨이지면 나누는게 무조건 좋다
while N != 1:
    r = N % K
    if r == 0:
        second += 1
        N /= K
    else:
        first += r
        N -= r

print(first + second)
