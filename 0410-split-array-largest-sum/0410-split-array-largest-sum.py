class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        def can_split(target_max):
            subarray_count = 1
            current_sum = 0            
            for num in nums:
                if current_sum + num > target_max:
                    subarray_count += 1
                    current_sum = num                    
                    if subarray_count > k:
                        return False
                else:
                    current_sum += num                    
            return True
        ans = high
        while low <= high:
            mid = low + (high - low) // 2            
            if can_split(mid):
                ans = mid       
                high = mid - 1 
            else:
                low = mid + 1   
        return ans
