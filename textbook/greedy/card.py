import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
card = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

print(N, M)
print(card)
