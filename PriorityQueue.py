class PQNode:
    def __init__(self, priority, hospital, ambulance, path):
        self.priority = priority
        self.hospital = hospital
        self.ambulance = ambulance
        self.path = path
        self.left = None
        self.right = None
        self.parent = None

class PriorityQueue:
    def __init__(self):
        self.root = None
        self.last_node = None
        self.size = 0
    
    def insert(self, item):
        priority, hospital, ambulance, path = item
        new_node = PQNode(priority, hospital, ambulance, path)
        self.size += 1
        
        if not self.root:
            self.root = new_node
            self.last_node = new_node
            return

        parent = self._find_parent_of_next_last()
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent
        self.last_node = new_node
        
        self._heapify_up(new_node)
    
    def extract_min(self):
        if not self.root:
            return None
        
        min_value = (self.root.priority, self.root.hospital, 
                    self.root.ambulance, self.root.path)
        
        if self.size == 1:
            self.root = None
            self.last_node = None
            self.size = 0
            return min_value
        
        if self.size == 2:
            min_value = (self.root.priority, self.root.hospital, 
                        self.root.ambulance, self.root.path)
            self.root = self.root.left if self.root.left else self.root.right
            self.root.parent = None
            self.last_node = self.root
            self.size = 1
            return min_value
        
        # Save last node's values
        last_priority = self.last_node.priority
        last_hospital = self.last_node.hospital
        last_ambulance = self.last_node.ambulance
        last_path = self.last_node.path
        
        # Remove last node
        if self.last_node.parent.right == self.last_node:
            self.last_node.parent.right = None
        else:
            self.last_node.parent.left = None
        
        # Update root
        self.root.priority = last_priority
        self.root.hospital = last_hospital
        self.root.ambulance = last_ambulance
        self.root.path = last_path
        
        self.size -= 1
        self.last_node = self._find_new_last()
        self._heapify_down(self.root)
        
        return min_value
    
    def _find_parent_of_next_last(self):
        if self.size == 1:
            return self.root
        path = bin(self.size + 1)[3:]
        node = self.root
        for i in range(len(path) - 1):
            if path[i] == '0':
                node = node.left
            else:
                node = node.right
        return node
    
    def _find_new_last(self):
        if self.size <= 1:
            return None
        path = bin(self.size)[3:]
        node = self.root
        for i in range(len(path)):
            if path[i] == '0':
                node = node.left
            else:
                node = node.right
        return node
    
    def _heapify_up(self, node):
        while node.parent and node.priority < node.parent.priority:
            self._swap(node, node.parent)
            node = node.parent
    
    def _heapify_down(self, node):
        while True:
            smallest = node
            if node.left and node.left.priority < smallest.priority:
                smallest = node.left
            if node.right and node.right.priority < smallest.priority:
                smallest = node.right
            if smallest == node:
                break
            self._swap(node, smallest)
            node = smallest
    
    def _swap(self, node1, node2):
        node1.priority, node2.priority = node2.priority, node1.priority
        node1.hospital, node2.hospital = node2.hospital, node1.hospital
        node1.ambulance, node2.ambulance = node2.ambulance, node1.ambulance
        node1.path, node2.path = node2.path, node1.path

    def is_empty(self):
        return self.root is None
