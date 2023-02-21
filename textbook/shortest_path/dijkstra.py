import sys
from collections import deque
from heapq import heappush, heappop

graph = [
    [None, 7, 9, None, None, 14],
    [7, None, 10, 15, None, None],
    [9, 10, None, 11, None, 2],
    [None, 15, 11, None, 6, None],
    [None, None, None, 6, None, 9],
    [14, None, 2, None, 9, None],
]

graph1 = [
    [None, 2, None, 1, None, None],
    [None, None, 3, 2, None, None],
    [None, 3, None, None, None, 5],
    [None, None, 3, None, 1, None],
    [None, None, 1, None, None, 2],
    [None, None, None, None, None, None],
]


def dijkstra(graph, start):
    length = len(graph)
    visited = [False for _ in range(length)]
    weight = [sys.maxsize for _ in range(length)]
    visited[start] = True
    weight[start] = 0

    queue = deque()
    queue.append(start)
    while queue:
        u = queue.pop()
        visited[u] = True

        for v in range(length):
            if graph[u][v] != None:
                weight[v] = min(weight[v], weight[u] + graph[u][v])

        idx = None
        for v in range(length):
            if not visited[v]:
                if idx == None or weight[idx] > weight[v]:
                    idx = v

        if idx != None:
            queue.append(idx)

    return weight


def enhanced_dijkstra(graph, start):
    queue = []
    weight = [sys.maxsize] * (len(graph))
    heappush(queue, (0, start))
    weight[start] = 0
    while queue:
        w, u = heappop(queue)

        if weight[u] < w:
            continue

        for v in range(len(graph)):
            if graph[u][v] != None:
                cost = w + graph[u][v]

                if cost < weight[v]:
                    weight[v] = cost
                    heappush(queue, (cost, v))
    return weight

def floyd_warshall(graph):
    num_node = len(graph)
    weight = [[sys.maxsize for _ in range(num_node)] for _ in range(num_node)]
    for i in range(num_node):
        for j in range(num_node):
            if i == j:
                weight[i][j] = 0
            elif graph[i][j] != None:
                weight[i][j] = graph[i][j] 
    
    for u in range(num_node):
        for k in range(num_node):
            for v in range(num_node):
                if weight[u][k] != None and weight[k][v] != None:
                    weight[u][v] = min(weight[u][v], weight[u][k] + weight[k][v])
    return weight

print(enhanced_dijkstra(graph1, 0))
print(enhanced_dijkstra(graph1, 1))
print(enhanced_dijkstra(graph1, 2))
print(enhanced_dijkstra(graph1, 3))
print(enhanced_dijkstra(graph1, 4))
print(enhanced_dijkstra(graph1, 5))
print(floyd_warshall(graph1))
