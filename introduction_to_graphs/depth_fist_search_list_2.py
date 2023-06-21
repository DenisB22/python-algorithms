def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = [
    [3, 6],
    [3, 6, 4, 5, 2],
    [1, 4, 5],
    [0, 1, 5],
    [6, 1, 2],
    [2, 1, 3],
    [4, 1, 0]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)

