class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def max_depth(self, root) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
t = Tree()
print(t.max_depth(root))
