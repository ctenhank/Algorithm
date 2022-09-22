n = int(input())
meetings = [input().split(' ') for _ in range(n)]

ans = 0
meeting = {}
for stime, etime in meetings:
    stime, etime = int(stime), int(etime)

    if etime not in meeting: meeting[etime] = []
    meeting[etime].append(meeting)

prev_etime = 0
for etime in sorted(list(meeting.keys())):
    stimes = sorted(meeting[etime])
    selected = False
    for stime in stimes:
        if stime == etime:
            ans += 1
            prev_etime = etime
        if not selected and stime >= prev_etime:
            selected = True
            ans += 1
            prev_etime = etime

print(ans)