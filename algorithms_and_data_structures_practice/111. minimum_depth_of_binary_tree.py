class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')

                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]

            print()
            v = vn


v = [20, 5, 24, 2, 16, 11, 18]
print(v)

t = Tree()
for x in v:
    t.append(Node(x))

t.del_node(5)

t.show_wide_tree(t.root)
