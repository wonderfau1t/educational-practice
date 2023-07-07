def find_paths(graph: dict, current_node: str, end: str, path=[]):
    """
    Finds ways from current node to end-node
    :param graph: Graph with nodes
    :param current_node: What node are we in now
    :param end: Destination node
    :param path: Path from to current node
    :return: List of paths
    """
    path = path + [current_node]

    if current_node == end:
        return [path]

    paths = []

    for node in graph[current_node]:
        new_paths = find_paths(graph, node, end, path)
        paths.extend(new_paths)

    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
end = 'F'

paths = find_paths(graph, start, end)
print(f'All ways from {start} to {end}: {paths}')
