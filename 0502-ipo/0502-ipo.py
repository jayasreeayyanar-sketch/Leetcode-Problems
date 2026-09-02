import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits), key=lambda x: x[0])        
        max_profit_heap = []
        project_idx = 0
        n = len(projects)
        for _ in range(k):
            while project_idx < n and projects[project_idx][0] <= w:
                heapq.heappush(max_profit_heap, -projects[project_idx][1])
                project_idx += 1
            if not max_profit_heap:
                break
            w += -heapq.heappop(max_profit_heap)            
        return w