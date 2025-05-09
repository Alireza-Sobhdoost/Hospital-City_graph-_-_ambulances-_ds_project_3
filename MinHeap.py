class Node:
    def __init__(self, f_score, node_id):
        self.f_score = f_score
        self.node_id = node_id
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None
        self.last_node = None
        self.size = 0
    
    def insert(self, item):
        f_score, node_id = item
        new_node = Node(f_score, node_id)
        self.size += 1
        
        if not self.root:
            self.root = new_node
            self.last_node = new_node
            return

        # Find the parent of the new last node
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
        
        min_value = (self.root.f_score, self.root.node_id)
        
        if self.size == 1:
            self.root = None
            self.last_node = None
            self.size = 0
            return min_value
            
        if self.size == 2:
            if self.root.left:
                self.root = self.root.left
            else:
                self.root = self.root.right
            self.root.parent = None
            self.last_node = self.root
            self.size = 1
            return min_value
        
        # Save the last node's values
        last_f_score = self.last_node.f_score
        last_node_id = self.last_node.node_id
        
        # Update parent pointers
        if self.last_node.parent.right == self.last_node:
            self.last_node.parent.right = None
        else:
            self.last_node.parent.left = None
            
        # Update root with last node's values
        self.root.f_score = last_f_score
        self.root.node_id = last_node_id
        
        # Find new last node
        self.size -= 1
        self.last_node = self._find_new_last()
        
        # Heapify down from root
        self._heapify_down(self.root)
        return min_value
    
    def _find_parent_of_next_last(self):
        if self.size == 1:
            return self.root
            
        path = bin(self.size + 1)[3:]  # Convert to binary and remove '0b1'
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
            
        path = bin(self.size)[3:]  # Convert to binary and remove '0b1'
        node = self.root
        for i in range(len(path)):
            if path[i] == '0':
                node = node.left
            else:
                node = node.right
        return node
    
    def _heapify_up(self, node):
        while node.parent and node.f_score < node.parent.f_score:
            # Swap values only
            node.f_score, node.parent.f_score = node.parent.f_score, node.f_score
            node.node_id, node.parent.node_id = node.parent.node_id, node.node_id
            node = node.parent
    
    def _heapify_down(self, node):
        while True:
            smallest = node
            if node.left and node.left.f_score < smallest.f_score:
                smallest = node.left
            if node.right and node.right.f_score < smallest.f_score:
                smallest = node.right
            if smallest == node:
                break
                
            # Swap values only
            node.f_score, smallest.f_score = smallest.f_score, node.f_score
            node.node_id, smallest.node_id = smallest.node_id, node.node_id
            node = smallest

