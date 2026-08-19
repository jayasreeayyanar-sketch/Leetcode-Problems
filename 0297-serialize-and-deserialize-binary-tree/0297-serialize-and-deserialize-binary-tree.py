class Codec:
    def serialize(self, root):
        res = []        
        def dfs(node):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ','.join(res)       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        tokens = data.split(',')
        token_iter = iter(tokens)        
        def dfs():
            try:
                val = next(token_iter)
            except StopIteration:
                return None                
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node            
        return dfs()
