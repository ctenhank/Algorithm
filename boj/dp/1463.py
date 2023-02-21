import sys
x = int(input())

dp = [sys.maxsize for _ in range(x + 1)]
dp[0] = -1

for i in range(1, x+1):
    if i % 2 == 0: dp[i] = min(dp[int(i/2)] + 1, dp[i])
    if i % 3 == 0: dp[i] = min(dp[int(i/3)] +1, dp[i])
    dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[x])