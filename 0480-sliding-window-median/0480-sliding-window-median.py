import heapq
from collections import defaultdict

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        max_heap = [] 
        min_heap = [] 
        lazy_remove = defaultdict(int)        
        def prune_max():
            while max_heap and lazy_remove[-max_heap[0]] > 0:
                lazy_remove[-max_heap[0]] -= 1
                heapq.heappop(max_heap)                
        
        def prune_min():
            while min_heap and lazy_remove[min_heap[0]] > 0:
                lazy_remove[min_heap[0]] -= 1
                heapq.heappop(min_heap)        
        def balance():
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                prune_max()
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
                prune_min()
        def add_num(num):
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            balance()
        def remove_num(num):
            lazy_remove[num] += 1
            if num <= -max_heap[0]:
                pass 
            prune_max()
            prune_min()
            balance()
        for i in range(k):
            add_num(nums[i])            
        def get_median():
            if k % 2 == 1:
                return float(-max_heap[0])
            else:
                return (-max_heap[0] + min_heap[0]) / 2.0
        res = [get_median()]
        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]
            balance_diff = -1 if out_num <= -max_heap[0] else 1
            lazy_remove[out_num] += 1
            if max_heap and in_num <= -max_heap[0]:
                balance_diff += 1
                heapq.heappush(max_heap, -in_num)
            else:
                balance_diff -= 1
                heapq.heappush(min_heap, in_num)
            if balance_diff > 0: 
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif balance_diff < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            prune_max()
            prune_min()
            
            res.append(get_median())            
        return res