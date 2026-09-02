class Solution(object):
    def reversePairs(self, nums):
        return self._merge_sort_and_count(nums, 0, len(nums) - 1)
    def _merge_sort_and_count(self, nums, left, right):
        if left >= right:
            return 0            
        mid = (left + right) // 2
        count = self._merge_sort_and_count(nums, left, mid)
        count += self._merge_sort_and_count(nums, mid + 1, right)
        count += self._count_pairs(nums, left, mid, right)
        self._merge(nums, left, mid, right)        
        return count
    def _count_pairs(self, nums, left, mid, right):
        count = 0
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))            
        return count
    def _merge(self, nums, left, mid, right):
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1                
        while i <= mid:
            temp.append(nums[i])
            i += 1            
        while j <= right:
            temp.append(nums[j])
            j += 1
        for k in range(len(temp)):
            nums[left + k] = temp[k]