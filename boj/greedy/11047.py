n, k = input().split(' ')
n, k = int(n), int(k)
a = [int(input()) for _ in range(n)]
a.reverse()

ans = 0
for e in a:
    q, r = divmod(k, e)
    ans += q
    k = r
print(ans)