class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n <= 1:
            return 0
        is_pal = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True
        dp = [0] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                min_cuts = i 
                for j in range(i, 0, -1):
                    if is_pal[j][i]:
                        min_cuts = min(min_cuts, dp[j - 1] + 1)
                dp[i] = min_cuts                
        return dp[n - 1]
