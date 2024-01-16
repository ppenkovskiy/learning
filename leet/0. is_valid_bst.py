class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_BST(root):
    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)

    result = []
    inorder_traversal(root, result)

    # Check if the result is sorted in ascending order
    for i in range(1, len(result)):
        if result[i] <= result[i - 1]:
            return False

    return True


# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_BST(root1))  # Output: True

# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(is_valid_BST(root2))  # Output: False
