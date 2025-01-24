class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)
    
    def extract_min(self):
        if not self.root:
            return None
        min_value = self.root.value
        if not self.root.left and not self.root.right:
            self.root = None
        else:
            self._remove_min(self.root)
        return min_value
    
    def _insert_node(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left:
                self._insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
                new_node.parent = current_node
                self._heapify_up(new_node)
        else:
            if current_node.right:
                self._insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node
                new_node.parent = current_node
                self._heapify_up(new_node)
    
    def _heapify_up(self, node):
        while node.parent and node.value < node.parent.value:
            self._swap(node, node.parent)
            node = node.parent
    
    def _heapify_down(self, node):
        while True:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right
            if smallest == node:
                break
            self._swap(node, smallest)
            node = smallest
    
    def _swap(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value
    
    def _remove_min(self, node):
        if node is None:
            return  # Base case to handle None nodes
        if node.left and (node.left.value < node.right.value if node.right else True):
            self._swap(node, node.left)
            self._remove_min(node.left)
        elif node.right:
            self._swap(node, node.right)
            self._remove_min(node.right)

