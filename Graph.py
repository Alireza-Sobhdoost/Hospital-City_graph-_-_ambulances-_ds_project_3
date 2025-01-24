from LinkedList import LinkedList
from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = LinkedList()

    def add_vertex(self, vertex_id, data=None, type=None):
        if not self.vertices.find(lambda v: v.id == vertex_id):
            self.vertices.append(Vertex(vertex_id, type, data))

    def add_edge_emergency(self, vertex1_id, vertex2_id, weight):
        vertex1 = self.vertices.find(lambda v: v.id == vertex1_id)
        vertex2 = self.vertices.find(lambda v: v.id == vertex2_id)
        if vertex1 and vertex2:
            vertex1.edges.append((vertex2_id, weight))
            vertex2.edges.append((vertex1_id, weight))

    def add_edge(self, vertex1_id, vertex2_id, weight):
        print(vertex1_id)
        vertex1 = self.vertices.find(lambda v: v.id == vertex1_id)
        print(vertex1)
        vertex2 = self.vertices.find(lambda v: v.id == vertex2_id)
        print(vertex2)
        if vertex1 and vertex2:
            vertex1.edges.append((vertex2_id, weight))
    def delete_vertex(self, vertex_id):
        vertex = self.vertices.delete(lambda v: v.id == vertex_id)
        if vertex:
            current = self.vertices.head
            while current:
                current.data.edges.delete(lambda e: e[0] == vertex_id)
                current = current.next

    def display(self):
        current = self.vertices.head
        while current:
            vertex = current.data
            print(f"{vertex.id} ({vertex.data}): ", end="")
            vertex.edges.display()
            current = current.next

# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A", "Data for A", "House")
    graph.add_vertex("B", "Data for B", "Hospital")
    graph.add_vertex("C", "Data for C", "AccessPoint")
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    graph.add_edge("A", "C", 3)
    graph.display()