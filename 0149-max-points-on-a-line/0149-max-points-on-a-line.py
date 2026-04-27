import collections
class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        ans = 1
        for i in range(n):
            slopes = collections.defaultdict(int)
            x1, y1 = points[i]            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = get_gcd(dx, dy)
                slope = (dx // g, dy // g)                
                slopes[slope] += 1
                ans = max(ans, slopes[slope] + 1)                
        return ans
