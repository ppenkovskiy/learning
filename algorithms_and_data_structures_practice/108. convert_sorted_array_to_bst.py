class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def sortedArrayToBST(self, nums):
        # base condition
        if len(nums) == 0:
            return None
        # set the middle node
        mid = len(nums) // 2
        # initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # assign left subtrees as the same function called on left subranges...
        root.left = self.sortedArrayToBST(nums[:mid])
        # assign right subtrees as the same function called on right subranges...
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        # return the root node...
        return root

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


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

root = BinarySearchTree().sortedArrayToBST(nums)
BinarySearchTree().show_wide_tree(root)
