class Solution(object):
    def nearestPalindromic(self, n):
        length = len(n)
        num = int(n)
        
        candidates = set()
        candidates.add(str(10**(length - 1) - 1))
        candidates.add(str(10**length + 1))
        
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])        
        for p in [prefix - 1, prefix, prefix + 1]:
            p_str = str(p)
            if length % 2 == 0:
                candidate = p_str + p_str[::-1]
            else:
                candidate = p_str + p_str[:-1][::-1]
            candidates.add(candidate)
            
        candidates.discard(n)
        
        closest = None
        min_diff = float('inf')        
        for cand in candidates:
            cand_num = int(cand)
            diff = abs(cand_num - num)
            if diff < min_diff or (diff == min_diff and cand_num < int(closest)):
                min_diff = diff
                closest = cand                
        return closest
