from collections import deque


def dfs(graph, node, visited, cycles, sorted_nodes):
    if node in visited:
        return
    if node in cycles:
        print("Invalid topological sorting")
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(graph, child, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)

graph = {}

nodes = int(input())

for _ in range(nodes):
    node, children = input().split('->')
    node = node.strip()
    children = children.split(', ') if children else []
    if children:
        children = [x.strip() for x in children]

    graph[node] = children

visited = set()
cycles = set()
sorted_nodes = deque()

for node in graph:
    dfs(graph, node, visited, cycles, sorted_nodes)

print(f'Topological sorting: {", ".join(sorted_nodes)}')