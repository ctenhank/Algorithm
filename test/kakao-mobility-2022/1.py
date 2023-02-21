def solution(flowers):
    bloomed = [0 for _ in range(365)]
    for blooming, falling in flowers:
        for date in range(blooming, falling):
            bloomed[date] = 1
    return sum(bloomed)