class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root=None):
        self.root = root

    def postorderTraversal(self, root):
        if root is None:
            return []

        result = []
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        return result


root = Node(20)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(16)
root.left.right.left = Node(11)
root.left.right.right = Node(18)
root.right = Node(24)

t = Tree(root)

print(t.postorderTraversal(root))
