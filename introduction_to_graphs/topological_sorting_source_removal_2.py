def find_dependencies(graph):
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


def find_nodes_without_dependancies(dependancies_by_node):
    for node, dependancies in dependancies_by_node.items():
        if dependancies == 0:
            return node

    return None


nodes = int(input())
sorted_elements = []
graph = {}

for _ in range(nodes):
    node, children = input().split('->')
    node = node.strip()
    children = [x.strip() for x in children.split(', ')] if children else []
    graph[node] = children
    # print(f'Node: {node}, Children: {children}')


dependancies_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependancies_by_node:
    node_to_remove = find_nodes_without_dependancies(dependancies_by_node)
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
