class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            length = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    matrix[nr][nc] > matrix[r][c]):

                    length = max(length, 1 + dfs(nr, nc))
            dp[r][c] = length
            return length
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))
        return result