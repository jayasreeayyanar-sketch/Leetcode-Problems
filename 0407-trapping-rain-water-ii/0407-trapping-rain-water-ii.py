import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0            
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True                    
        total_water = 0
        max_boundary = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while min_heap:
            height, r, c = heapq.heappop(min_heap)
            max_boundary = max(max_boundary, height)            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    neighbor_height = heightMap[nr][nc]
                    if neighbor_height < max_boundary:
                        total_water += max_boundary - neighbor_height
                    heapq.heappush(min_heap, (neighbor_height, nr, nc))                    
        return total_water