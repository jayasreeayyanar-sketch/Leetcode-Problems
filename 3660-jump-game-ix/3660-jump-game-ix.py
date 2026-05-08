class Solution:
    def maxValue(self, nums):
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        ans = [0] * n
        start = 0
        curr_max = nums[0]
        for i in range(n - 1):
            curr_max = max(curr_max, nums[i])
            if curr_max <= suffix_min[i + 1]:
                comp_max = max(nums[start:i + 1])
                for j in range(start, i + 1):
                    ans[j] = comp_max
                start = i + 1
                curr_max = nums[start]
        comp_max = max(nums[start:])
        for j in range(start, n):
            ans[j] = comp_max
        return ans
sol = Solution()
print(sol.maxValue([2,1,3]))   # [2,2,3]
print(sol.maxValue([2,3,1]))   # [3,3,3]
print(sol.maxValue([4,1,3,2])) # [4,4,4,4]