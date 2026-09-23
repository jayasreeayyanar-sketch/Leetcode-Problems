class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0            
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]        
        
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far                
            
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)            
            result = max(result, max_so_far)            
            
        return result
