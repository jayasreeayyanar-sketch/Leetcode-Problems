class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1          
        while k > 0:
            steps = self._count_steps(n, curr, curr + 1)            
            if steps <= k:
                k -= steps
                curr += 1  
            else:
                k -= 1
                curr *= 10                 
        return curr
    def _count_steps(self, n, first, last):
        """Helper to calculate how many numbers exist between prefix 'first' and 'last'."""
        steps = 0
        while first <= n:
            steps += min(n + 1, last) - first
            first *= 10
            last *= 10
        return steps