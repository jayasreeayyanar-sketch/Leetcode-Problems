from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []            
        result = []
        q = deque() 
        
        for i, num in enumerate(nums):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if i >= k - 1:
                result.append(nums[q[0]])                
        return result