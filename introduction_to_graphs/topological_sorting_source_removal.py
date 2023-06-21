def find_dependancies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependancies(dependancies_by_node):
    for node, dependancies in dependancies_by_node.items():
        if dependancies == 0:
            return node
    return None


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children


dependancies_by_node = find_dependancies(graph)
has_cycles = False
sorted_nodes = []

while dependancies_by_node:
    node_to_remove = find_node_without_dependancies(dependancies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependancies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependancies_by_node[child] -= 1

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
