from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_at_j = dp[j][diff]
                total_count += count_at_j
                dp[i][diff] += count_at_j + 1                
        return total_count