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
        # Initialize the open and closed sets
        open_set = MinHeap()
        open_set.insert((0, start_id))
        closed_set = set()
        
        # Path tracking
        came_from = {}
        g_score = {start_id: 0}
        
        while open_set.root:
            current_f_score, current_id = open_set.extract_min()
            
            # Skip if we've already processed this node
            if current_id in closed_set:
                continue
                
            # Add to closed set
            closed_set.add(current_id)
            
            # Check if we reached the goal
            if current_id == goal_id:
                path = []
                while current_id in came_from:
                    path.append(current_id)
                    current_id = came_from[current_id]
                path.append(start_id)
                return path[::-1]
            
            # Get current vertex
            current_vertex = self.vertices.find(lambda v: v.id == current_id)
            if not current_vertex:
                continue
                
            # Check all neighbors
            edges = current_vertex.edges
            current_edge = edges.head
            while current_edge:
                neighbor_id, weight = current_edge.data
                
                # Skip if in closed set
                if neighbor_id in closed_set:
                    current_edge = current_edge.next
                    continue
                
                # Calculate tentative g score
                tentative_g = g_score[current_id] + weight
                
                if neighbor_id not in g_score or tentative_g < g_score[neighbor_id]:
                    came_from[neighbor_id] = current_id
                    g_score[neighbor_id] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor_id, goal_id)
                    open_set.insert((f_score, neighbor_id))
                
                current_edge = current_edge.next
        
        return None

    def calculate_path_cost(self, path):
        if not path or len(path) < 2:
            return 0
        
        cost = 0
        for i in range(len(path) - 1):
            current = self.vertices.find(lambda v: v.id == path[i])
            if current:
                edge = current.edges.find(lambda e: e[0] == path[i + 1])
                if edge:
                    cost += edge[1]
        return cost



# H1 (s): ('A1', 2) -> None
# H2 (g): ('A2', 4) -> None
# A1 (A1): ('H1', 2) -> ('A2', 4) -> ('M1', 5) -> ('M2', 1) -> None
# A2 (A2): ('A1', 2) -> ('H2', 3) -> None
# M1 (M1): ('A1', 2) -> None
# M2 (M2): ('A1', 3) -> None
graph = Graph()

# Add vertices
graph.add_vertex("H1", "s")
graph.add_vertex("H2", "g")
graph.add_vertex("A1", "A1")
graph.add_vertex("A2", "A2")
graph.add_vertex("M1", "M1")
graph.add_vertex("M2", "M2")

# Add edges
graph.add_edge("H1", "A1", 2)
graph.add_edge("H2", "A2", 4)
graph.add_edge("A1", "H1", 2)
graph.add_edge("A1", "A2", 4)
graph.add_edge("A1", "M1", 5)
graph.add_edge("A1", "M2", 1)
graph.add_edge("A2", "A1", 2)
graph.add_edge("A2", "H2", 3)
graph.add_edge("M1", "A1", 2)
graph.add_edge("M2", "A1", 3)

# Display the graph
graph.display()

# Test A* search from H1 to H2
path = graph.a_star_search("H2", "M1")
if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Path cost: {graph.calculate_path_cost(path)}")
else:
    print("No path found")