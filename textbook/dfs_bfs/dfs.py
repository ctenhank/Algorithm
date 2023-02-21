def _dfs_recursive(graph, u, visited, sequence):
    visited[u] = True
    sequence.append(u)
    for v in graph[u]:
        if not visited[v]:
            sequence = _dfs_recursive(graph, v, visited, sequence)
    return sequence


def dfs_recursive(graph, start):
    visited = [False for _ in range(len(graph) + 1)]
    sequence = []
    visited[start] = True
    sequence.append(start)

    for v in graph[start]:
        if not visited[v]:
            sequence = _dfs_recursive(graph, v, visited, sequence)
    return sequence


def dfs_iterative(graph, start):
    stack = []
    visited = [False for _ in range(len(graph))]
    sequence = []

    stack.append(start)
    visited[start] = True

    while stack:
        u = stack.pop()
        sequence.append(u)
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True

    return sequence


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]


print(f"Recursive DFS: {dfs_recursive(graph, 1)}")
print(f"Iterative DFS: {dfs_iterative(graph, 1)}")
