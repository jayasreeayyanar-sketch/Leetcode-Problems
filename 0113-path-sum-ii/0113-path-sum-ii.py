class Solution(object):
    def pathSum(self, root, targetSum):
        result = []        
        def dfs(node, current_sum, path):
            if not node:
                return
            path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(path))
            else:
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
            path.pop()            
        dfs(root, 0, [])
        return result
