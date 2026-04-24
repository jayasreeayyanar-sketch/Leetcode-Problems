class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, current_num):
            if not node:
                return 0
            current_num = current_num * 10 + node.val
            if not node.left and not node.right:
                return current_num
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        return dfs(root, 0)
