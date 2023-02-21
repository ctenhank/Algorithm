# 문제
# 카운터에 500, 100, 50, 10원짜리 동전이 무한대로 존재할 때,
# 손님에게 거슬러 줘야 할 돈이 N원일 때 동전의 최소 개수를 구해라

N = 1260

nchange = 0
coin = [500, 100, 50, 10]

left = N
for c in coin:
    nc = left // c
    nchange += nc
    left -= c * nc

print(nchange)
