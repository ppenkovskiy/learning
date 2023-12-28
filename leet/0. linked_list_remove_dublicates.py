class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_trees_equal(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and tree2:
        return (tree1.value == tree2.value and
                are_trees_equal(tree1.left, tree2.left) and
                are_trees_equal(tree1.right, tree2.right))
    else:
        return False

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print(are_trees_equal(tree1, tree2))