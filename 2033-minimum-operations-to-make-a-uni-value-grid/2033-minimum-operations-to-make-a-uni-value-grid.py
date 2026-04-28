class Solution(object):
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            nums.extend(row)
        base_mod = nums[0] % x
        for num in nums:
            if num % x != base_mod:
                return -1
        nums.sort()
        median = nums[len(nums) // 2]
        operations = 0
        for num in nums:
            operations += abs(num - median) // x            
        return operations
