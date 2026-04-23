class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.build(1, n)
    def build(self, start, end):
        if start > end:
            return [None]
        trees = []
        for root_val in range(start, end + 1):
            left_trees = self.build(start, root_val - 1)
            right_trees = self.build(root_val + 1, end)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees