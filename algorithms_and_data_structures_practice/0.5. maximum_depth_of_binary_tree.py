class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root=None):
        self.root = root

    def maximum_depth(self, root):
        if root is None:
            return 0

        max_depth = 0

        v = [root]

        while v:
            vn = []
            for x in v:
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
            max_depth += 1

        return max_depth

    # def maximum_depth(self, root):
    #     if root is None:
    #         return 0
    #     left_depth = self.maximum_depth(root.left)
    #     right_depth = self.maximum_depth(root.right)
    #     return max(left_depth, right_depth) + 1


root = Node(20)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(16)
root.left.right.left = Node(11)
root.left.right.right = Node(18)
root.right = Node(24)

t = Tree(root)

print(t.maximum_depth(root))
