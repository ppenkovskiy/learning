class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# breadth first search.
def breadth_first_search(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


# example usage:
# constructing a simple binary tree:
#         1
#        / \
#       2   3
#      / \
#     10  4
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(10)
root.left.right = Node(4)

# perform BFS and print the result
result_bfs = breadth_first_search(root)
print("Breadth-First Search:", result_bfs)
