n = int(input())
meetings = [input().split(' ') for _ in range(n)]

meeting = {}
for stime, etime in meetings:
    stime, etime = int(stime), int(etime)

    if etime not in meeting: meeting[etime] = []
    meeting[etime].append(stime)

ans = 0
prev_etime = 0
for etime in sorted(list(meeting.keys())):
    selected = False
    for stime in sorted(meeting[etime]):
        if not selected and stime >= prev_etime:
            selected = True
            ans += 1
            prev_etime = etime
        # 그냥 if했을 떄 중복 문제가 발생할 수 있음
        elif stime == etime:
            ans += 1
            prev_etime = etime

        
print(ans)