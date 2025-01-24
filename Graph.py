from LinkedList import LinkedList
from Vertex import Vertex
from MinHeap import MinHeap

class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

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

    def get_score(self, scores_list, node_id):
        pair = scores_list.find(lambda x: x.key == node_id)
        return pair.value if pair else None

    def set_score(self, scores_list, node_id, value):
        pair = scores_list.find(lambda x: x.key == node_id)
        if pair:
            pair.value = value
        else:
            scores_list.append(KeyValuePair(node_id, value))

    def heuristic(self, current_id, goal_id):
        return 0 if current_id == goal_id else 1

    def a_star_search(self, start_id, goal_id):
        # Min-Heap for the open set
        open_set = MinHeap()
        open_set.insert((0, start_id))  # (f_score, node_id)

        # Dictionaries to store scores and paths
        g_scores = {start_id: 0}  # Cost from start to each node
        f_scores = {start_id: self.heuristic(start_id, goal_id)}  # Estimated total cost
        came_from = {}  # To reconstruct the path

        while open_set.root:  # While there are nodes to explore
            # Get node with the lowest f_score
            _, current = open_set.extract_min()

            # If we reached the goal
            if current == goal_id:
                # Reconstruct the path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start_id)
                path.reverse()
                return path

            # Find the current vertex in the graph
            current_vertex = self.vertices.find(lambda v: v.id == current)
            if current_vertex:
                current_edges = current_vertex.edges
                current_node = current_edges.head

                while current_node:  # Traverse neighbors
                    neighbor_id, weight = current_node.data
                    tentative_g_score = g_scores[current] + weight

                    # If this path to the neighbor is better, record it
                    if neighbor_id not in g_scores or tentative_g_score < g_scores[neighbor_id]:
                        came_from[neighbor_id] = current  # Record path
                        g_scores[neighbor_id] = tentative_g_score
                        f_scores[neighbor_id] = tentative_g_score + self.heuristic(neighbor_id, goal_id)

                        # Add neighbor to the open set
                        open_set.insert((f_scores[neighbor_id], neighbor_id))

                    current_node = current_node.next  # Move to the next neighbor

        # If we exhaust the open set without finding the goal
        return None

    def calculate_path_cost(self, path):
        if not path or len(path) < 2:
            return float('inf')
        
        total_cost = 0
        for i in range(len(path) - 1):
            current = self.vertices.find(lambda v: v.id == path[i])
            if current:
                edge = current.edges.find(lambda e: e[0] == path[i + 1])
                if edge:
                    total_cost += edge[1]
                else:
                    return float('inf')
        return total_cost

# graph = Graph()
# graph.add_vertex("A1", "A1")
# graph.add_vertex("M1", "M1")
# graph.add_vertex("H1", "Ghaem")

# graph.add_edge("A1", "M1", 4)
# graph.add_edge("A1", "H1", 3)
# graph.add_edge("H1", "A1", 2)
# graph.add_edge("M1", "A1", 3)

# # Run A* Search
# path = graph.a_star_search("H1", "M1")
# if path:
#     print(f"Path found: {' -> '.join(path)}")
# else:
#     print("No path found")
