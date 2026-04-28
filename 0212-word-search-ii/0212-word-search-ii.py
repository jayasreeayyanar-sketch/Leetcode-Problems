class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = None  

class Solution(object):
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = word
            
        rows, cols = len(board), len(board[0])
        result = []
        def backtrack(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]
            if curr_node.is_word:
                result.append(curr_node.is_word)
                curr_node.is_word = None 
            board[r][c] = "#"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    backtrack(nr, nc, curr_node)
            board[r][c] = char            
            if not curr_node.children:
                parent.children.pop(char)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtrack(r, c, root)                    
        return result
