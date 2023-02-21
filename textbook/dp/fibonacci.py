def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


dp = {0: 1, 1: 1}


def fibonacci_recursive(n):
    if n in dp:
        return dp[n]
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


def fibonacci_iterative(n):
    for i in range(2, n + 1):
        if i in dp:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = 10000
dp = [0 for _ in range(n)]
dp[0], dp[1] = 1, 1


def fibonacci_recursive(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


def fibonacci_iterative(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
