class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self, node):
        if node is None:
            return []

        result = []
        result += self.inorder_traversal(node.left)
        result.append(node.data)
        result += self.inorder_traversal(node.right)
        return result


root = Node(20)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(16)
root.left.right.left = Node(11)
root.left.right.right = Node(18)
root.right = Node(24)

t = Tree(root)

print(t.inorder_traversal(root))
