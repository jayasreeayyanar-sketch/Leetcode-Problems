class Solution(object):
    def findItinerary(self, tickets):
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        result = []
        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            result.append(airport)
        dfs("JFK")
        return result[::-1]