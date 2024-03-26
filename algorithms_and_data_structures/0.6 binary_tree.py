class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __find(self, node, parent, value):
        """The __find method is a recursive helper function for finding
        a node with a specific value in the tree. It returns the  found
        node, its parent, and a boolean indicating  whether  the  value
        was found."""

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
        """The append method adds a new node to the tree while maintaining the binary
        tree property. If the tree is empty, the new node becomes the root. Otherwise,
        it uses the __find method to locate the appropriate position for the new node."""

        if self.root is None:
            self.root = obj
            return obj

        # parent:None - cs parent node for root == None
        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


    def show_wide_tree(self, node):
        if node is None:
            return
        # v - list of nodes of current level
        v = [node]
        while v:
            # vn - list of nodes of the next level
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        # s - node you want to delete
        # p - parent of the node you want to delete
        # fl_find (flag find) - is this node (s) exists in the tree
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()
for x in v:
    t.append(Node(x))

t.show_tree(t.root)
