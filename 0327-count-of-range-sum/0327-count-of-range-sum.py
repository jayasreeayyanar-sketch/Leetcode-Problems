class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        def merge_sort(left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2

            count = merge_sort(left, mid) + merge_sort(mid, right)
            j = k = mid
            for i in range(left, mid):
                while k < right and prefix[k] - prefix[i] < lower:
                    k += 1
                while j < right and prefix[j] - prefix[i] <= upper:
                    j += 1
                count += j - k
            prefix[left:right] = sorted(prefix[left:right])
            return count
        return merge_sort(0, len(prefix))