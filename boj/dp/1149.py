N = int(input())
cost = []
RED, GREEN, BLUE = 0, 1, 2
dp = [[0 for _ in range(N+1)] for _ in range(3)]
for i in range(1, N+1):
    r, g, b = input().split(' ')
    cost.append((int(r), int(g), int(b)))

for i in range(1, N+1):
    dp[RED][i] = cost[i-1][RED] + min(dp[GREEN][i-1], dp[BLUE][i-1])
    dp[GREEN][i] = cost[i-1][GREEN]  + min(dp[RED][i-1], dp[BLUE][i-1]) 
    dp[BLUE][i] = cost[i-1][BLUE]  + min(dp[GREEN][i-1], dp[RED][i-1])

print(min([dp[RED][N], dp[GREEN][N], dp[BLUE][N]]))