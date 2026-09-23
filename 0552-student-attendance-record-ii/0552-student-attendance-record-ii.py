class Solution(object):
    def checkRecord(self, n):
        MOD = 10**9 + 7
        
        dp = [[0] * 3 for _ in range(2)]
        
        dp[0][0] = 1 
        
        dp[1][0] = 1 
        
        dp[0][1] = 1 
        
        for day in range(2, n + 1):
            next_dp = [[0] * 3 for _ in range(2)]
            
            next_dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            next_dp[1][0] = (dp[1][0] + dp[1][1] + dp[1][2]) % MOD
            
            next_dp[1][0] = (next_dp[1][0] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            
            next_dp[0][1] = dp[0][0]
            next_dp[0][2] = dp[0][1]
            next_dp[1][1] = dp[1][0]
            next_dp[1][2] = dp[1][1]            
            dp = next_dp
        return sum(sum(row) for row in dp) % MOD
