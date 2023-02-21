import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
B.sort()

start = 0
end = len(A) - 1
ret = sum(A)
for i in range(K):
    A[start + i] = B[end - i]
    ret = max(ret, sum(A))
print(ret)
