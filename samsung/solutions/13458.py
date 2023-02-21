N = int(input())
A = [int(e) for e in input().split(' ')]
B, C = [int(e) for e in input().split(' ')]

ans = 0
for i in range(len(A)):
    A[i] -= B
    if A[i] < 0:
        A[i] = 0
    ans += 1

    q, r = divmod(A[i], C)
    ans += q
    if r > 0:
        ans += 1

print(ans)