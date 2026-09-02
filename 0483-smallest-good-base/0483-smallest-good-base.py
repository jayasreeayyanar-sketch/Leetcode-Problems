class Solution(object):
    def smallestGoodBase(self, n):
        num = int(n)
        for m in range(60, 1, -1):
            left = 2
            right = int(num ** (1.0 / (m - 1))) + 1            
            while left <= right:
                mid = (left + right) // 2
                current_sum = 0
                for _ in range(m):
                    current_sum = current_sum * mid + 1                    
                if current_sum == num:
                    return str(mid)
                elif current_sum < num:
                    left = mid + 1
                else:
                    right = mid - 1                    
        return str(num - 1)
