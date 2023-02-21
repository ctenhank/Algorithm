from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


def bfs(graph, start):
    queue = deque()
    visited = [False for _ in range(len(graph))]
    sequence = []
    visited[start] = True
    queue.append(start)
    while queue:
        u = queue.popleft()
        sequence.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return sequence


print(f"BFS: {bfs(graph, 1)}")
