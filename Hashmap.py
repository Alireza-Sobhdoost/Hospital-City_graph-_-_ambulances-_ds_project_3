class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Node:
    """Node for a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class HashedLinkedList:
    """Custom linked list to manage collisions in hash map buckets."""
    def __init__(self):
        self.head = None

    def push(self, data):
        """Manually add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def pop(self, condition):
        """Manually remove a node that meets the condition."""
        current = self.head
        prev = None

        while current:
            if condition(current.data):
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return current.data
            prev = current
            current = current.next
        return None

    def find(self, condition):
        """Find a node that matches the condition."""
        current = self.head
        while current:
            if condition(current.data):
                return current.data
            current = current.next
        return None

    def display(self):
        """Display all nodes in the linked list."""
        current = self.head
        while current:
            print(f"({current.data.key}, {current.data.value})", end=" -> ")
            current = current.next
        print("None")

class HashMap:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.count = 0
        self.buckets = [HashedLinkedList() for _ in range(self.size)]
    
    def _hash(self, key):
        """Generate a hash value for the given key."""
        return hash(key) % self.size
    
    def _resize(self):
        """Double the size of the hash map when 80% full."""
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [HashedLinkedList() for _ in range(self.size)]
        self.count = 0

        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.put(current.data.key, current.data.value)
                current = current.next
    
    def put(self, key, value):
        """Insert or update a key-value pair."""
        if self.count >= 0.8 * self.size:
            self._resize()
        
        index = self._hash(key)
        bucket = self.buckets[index]

        existing_pair = bucket.find(lambda x: x.key == key)
        if existing_pair:
            existing_pair.value = value  # Update existing key
        else:
            bucket.push(KeyValuePair(key, value))
            self.count += 1
    
    def get(self, key):
        """Retrieve the value for a given key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        pair = bucket.find(lambda x: x.key == key)
        return pair.value if pair else None
    
    def remove(self, key):
        """Remove a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        removed_pair = bucket.pop(lambda x: x.key == key)
        if removed_pair:
            self.count -= 1
            return True
        return False
    
    def display(self):
        """Display the contents of the hash map."""
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: ", end="")
            bucket.display()
