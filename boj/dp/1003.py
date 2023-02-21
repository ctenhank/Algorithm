T = int(input())

ans = []
while T:
    n = int(input())
    dp = [(1, 0) for _ in range(n + 1)]
    if n >= 1: dp[1] = (0, 1)

    for i in range(2, n + 1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    ans.append((dp[n][0], dp[n][1]))
    
    T -= 1

for a in ans:
    print(f'{a[0]} {a[1]}')