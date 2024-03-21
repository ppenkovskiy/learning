class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            # going to the end of the list
            while current_node.next_node:
                current_node = current_node.next_node

            # appending new node to the end of the list
            current_node.next_node = new_node

    # prepend - adding new node to the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print(" -> ".join(map(str, elements)))


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()  # output: 1 -> 2 -> 3

linked_list.prepend(0)
linked_list.display()  # output: 0 -> 1 -> 2 -> 3

linked_list.delete(2)
linked_list.display()  # output: 0 -> 1 -> 3

linked_list.delete(3)
linked_list.display()
