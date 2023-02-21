import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)
first, second = arr[0], arr[1]

q, r = divmod(M, (K + 1))
summation = K * first + second
ret = q * summation + K * r
print(ret)


# ret = 0

# while M > 0:
#    for i in range(K):
#        if M <= 0:
#            break
#        ret += arr[0]
#        M -= 1

#    if M > 0:
#        ret += arr[1]
#        M -= 1

# print(ret)
