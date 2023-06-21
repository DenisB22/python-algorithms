def dfs(node, graph, visited, connected_component):

    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, connected_component)

    if node not in connected_component:
        connected_component.append(node)


nodes = int(input())
graph = []

for _ in range(nodes):
    graph.append([int(x) for x in input().split()])

visited = [False] * nodes

for node in range(nodes):
    connected_component = []
    dfs(node, graph, visited, connected_component)
    if connected_component:
        print(f"Connected component: {' '.join(str(x) for x in connected_component)}")