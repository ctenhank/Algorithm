n = int(input())
p = input().split(' ')
p_ = [int(e) for e in p]
p = p_
p.sort()

time = []
prev = 0
for e in p:
    time.append((prev + e))
    prev = prev + e

print(sum(time))
