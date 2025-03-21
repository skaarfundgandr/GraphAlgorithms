from Graph import Graph, Vertex
from collections import deque

def topological_sort(graph):
    in_degree = {vertex: 0 for vertex in graph.vertices.values()}

    for vertex in graph:
        for neighbor in vertex.get_connections():
            in_degree[neighbor] += 1

    queue = deque([vertex for vertex in graph if in_degree[vertex] == 0])
    topo_order = []

    while queue:
        vertex = queue.popleft()
        topo_order.append(vertex.key)

        for neighbor in vertex.get_connections():
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(graph.vertices):
        raise ValueError("Graph has at least one cycle, topological sorting not possible.")

    return topo_order

# Example usage:
g = Graph()
g.add_edge("A", "C")
g.add_edge("B", "C")
g.add_edge("C", "D")

topo_sorted = topological_sort(g)
print("Topological Sort:", topo_sorted)
