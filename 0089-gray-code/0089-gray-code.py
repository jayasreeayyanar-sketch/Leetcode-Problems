class Solution(object):
    def grayCode(self, n):
        result = []        
        for i in range(1 << n): 
            gray = i ^ (i >> 1)
            result.append(gray)            
        return result