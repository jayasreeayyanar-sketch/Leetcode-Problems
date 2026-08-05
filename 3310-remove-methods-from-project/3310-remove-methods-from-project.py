class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        suspicious = set()
        queue = [k]
        suspicious.add(k)        
        while queue:
            curr = queue.pop(0)
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]