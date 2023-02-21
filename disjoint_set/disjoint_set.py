import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
operations = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]


class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            self.parent[v] = u

    def find(self, u):
        """트리 구조가 일자형이면 O(n) 걸리므로 비효율적"""
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])


class DisjointSet2:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n + 1)]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            u, v = v, u

        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])


class DisjointSet3:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n + 1)]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            u, v = v, u

        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]


disjoint_set = DisjointSet3(n)
for op, a, b in operations:
    if a > b:
        a, b = b, a

    if op == 0:
        disjoint_set.union(a, b)
    else:
        a = disjoint_set.find(a)
        b = disjoint_set.find(b)
        print("YES" if a == b else "No")
