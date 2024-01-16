class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = None

    def isSymmetric(self):
        def is_mirror(left, right):
            # base case: if both nodes are None, they are symmetric.
            if not left and not right:
                return True
            # if one of the nodes is None or values are not equal, not symmetric.
            if not left or not right or left.val != right.val:
                return False
            # recursively check the subtrees in a mirrored fashion.
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        # check if the tree is symmetric starting from the root.
        return is_mirror(self.root, self.root)


# Create nodes and construct the tree
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

# Create the Tree instance
t = Tree(root)

# Check if the tree is symmetric
result = t.isSymmetric()
print(result)
