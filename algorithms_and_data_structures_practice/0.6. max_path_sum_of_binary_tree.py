class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_sum(root: TreeNode) -> int:
    if root is None:
        return 0
    elif root.left is None:
        return root.value + max_sum(root.right)
    elif root.right is None:
        return root.value + max_sum(root.left)
    else:
        return root.value + max(max_sum(root.left), max_sum(root.right))
