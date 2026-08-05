class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False            
        buckets = {}
        width = valueDiff + 1        
        for i, num in enumerate(nums):
            bucket_id = num // width
            if bucket_id in buckets:
                return True
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            buckets[bucket_id] = num
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // width
                del buckets[old_bucket_id]                
        return False