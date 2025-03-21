class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbours = {} # Dictionary that keeps track of the list of neighbors

    def add_neighbor(self, neighbor, weight=0):
        self.neighbours[neighbor] = weight

    def get_connections(self) -> list[any]:
        return self.neighbours.keys()

    def get_weight(self, neighbor) -> int:
        return self.neighbours[neighbor] # Returns the weight (value) of the neighbor

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key) -> Vertex:
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))

        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))

        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)

    def get_vertices(self) -> list[any]:
        return self.vertices.keys()

    # Magic Methods
    def __contains__(self, key): # For use with the 'in' operator e.g. if x in y
        return key in self.vertices

    def __iter__(self): # Returns an iterator for looping which contains vertices in the graph
        return iter(self.vertices.values())