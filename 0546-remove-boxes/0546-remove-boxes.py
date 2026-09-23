class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        memo = {}        
        def calculatePoints(i, j, k):
            if i > j:
                return 0
            state = (i, j, k)
            if state in memo:
                return memo[state]
            while i + 1 <= j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
            res = (k + 1) * (k + 1) + calculatePoints(i + 1, j, 0)
            for m in range(i + 1, j + 1):
                if boxes[i] == boxes[m]:
                    res = max(res, calculatePoints(i + 1, m - 1, 0) + calculatePoints(m, j, k + 1))                    
            memo[state] = res
            return res            
        return calculatePoints(0, len(boxes) - 1, 0)
