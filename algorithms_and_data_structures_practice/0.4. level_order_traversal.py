class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def __init__(self, root=None):
        self.root = root

    def levelorderTraversal(self, root):
        if root is None:
            return

        result = []

        # v - list of nodes of current level
        v = [root]

        while v:
            # vn - list of nodes of the next level
            vn = []
            res_n = []
            for x in v:
                res_n.append(x.val)
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
            result.append(res_n)

        return result


root = Node(20)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(16)
root.left.right.left = Node(11)
root.left.right.right = Node(18)
root.right = Node(24)

t = Tree(root)

print(t.levelorderTraversal(root))
