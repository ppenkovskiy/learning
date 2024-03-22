class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def min_depth(self, node):
        if node is None:
            return 0

        v = [node]
        depth = 0
        while v:
            depth += 1

            vn = []
            for x in v:
                if x.left:
                    vn += [x.left]
                else:
                    return depth
                if x.right:
                    vn += [x.right]
                else:
                    return depth

            v = vn
        return depth


v = [20, 5, 24, 2, 16, 11, 18] # 2

t = Tree()
for x in v:
    t.append(Node(x))

print(t.min_depth(t.root))
