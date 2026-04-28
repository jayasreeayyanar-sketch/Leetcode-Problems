import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))
        events.sort()
        
        res = [[0, 0]]
        max_heap = [0]    
        
        to_remove = {}
        
        for x, h in events:
            if h < 0:
                heapq.heappush(max_heap, h)
            else:     
                to_remove[h] = to_remove.get(h, 0) + 1
            while -max_heap[0] in to_remove and to_remove[-max_heap[0]] > 0:
                h_to_rem = -max_heap[0]
                to_remove[h_to_rem] -= 1
                heapq.heappop(max_heap)
            curr_max = -max_heap[0]
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
        
        return res[1:] 
