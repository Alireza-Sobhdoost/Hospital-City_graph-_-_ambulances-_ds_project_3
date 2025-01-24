class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def find(self, condition):
        current = self.head
        while current:
            if condition(current.data):
                return current.data
            current = current.next
        return None

    def delete(self, condition):
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
    
    def __len__ (self):
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.next
        return count

    def get_by_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")