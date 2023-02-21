import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
tteok = list(map(int, sys.stdin.readline().rstrip().split()))
tteok.sort()


def slice(length):
    ret = 0
    for t in tteok:
        left = t - length
        ret += 0 if left <= 0 else left
    return ret


def binary_search(M):
    left, right = 0, 2000000000
    height = 0
    while left <= right:
        mid = int((left + right) / 2)
        tteok_length = slice(mid)

        if tteok_length >= M:
            left = mid + 1
            height = max(height, mid)
        elif tteok_length < M:
            right = mid - 1
    return height


print(binary_search(M))
