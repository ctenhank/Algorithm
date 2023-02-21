import sys

N = int(sys.stdin.readline().rstrip())
grade = [sys.stdin.readline().rstrip().split() for _ in range(N)]
grade = [[g[0], int(g[1])] for g in grade]
grade.sort(key=lambda e: e[1])

for name, _ in grade:
    print(name)
