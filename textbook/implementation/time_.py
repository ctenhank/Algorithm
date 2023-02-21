import sys

N = int(sys.stdin.readline().rstrip())
# 3초마다 증가
ret = 0
current = 0
finish = 3600 * N + 60 * 59 + 59
while current <= finish:
    hour = int(current / 3600)
    minute, second = divmod((current - hour * 3600), 60)
    if "3" in str(hour):
        ret += 1
    elif "3" in str(minute):
        ret += 1
    elif "3" in str(second):
        ret += 1
    current += 1
print(ret)
