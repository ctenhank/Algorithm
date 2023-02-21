T = int(input())

ans = []
while T:
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp = [0, 1, 1, 1]
    if n > 3:
        for _ in range(4, n + 1): dp.append(0)

    for i in range(1, n + 1):
        # dp[i] += dp[i-1] + 1 -> 겹치는 경우가 있음
        # Ex: (1 + 1 + 2), (1 + 2 + 1) -> 동일한 케이스
        if i - 1 >= 0: dp[i] += dp[i-1]
        if i - 2 >= 0: dp[i] += dp[i-2]
        if i - 3 >= 0: dp[i] += dp[i-3]
    ans.append(dp[n])
    
    T -= 1

for a in ans:
    print(a)