from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):
        ring_len = len(ring)
        char_to_indices = defaultdict(list)
        for idx, char in enumerate(ring):
            char_to_indices[char].append(idx)            
        memo = {}        
        def dp(key_idx, ring_idx):
            if key_idx == len(key):
                return 0                
            state = (key_idx, ring_idx)
            if state in memo:
                return memo[state]                
            min_total_steps = float('inf')
            target_char = key[key_idx]            
            for next_ring_idx in char_to_indices[target_char]:
                linear_dist = abs(ring_idx - next_ring_idx)
                rotation_steps = min(linear_dist, ring_len - linear_dist)
                total_steps = rotation_steps + 1 + dp(key_idx + 1, next_ring_idx)
                
                min_total_steps = min(min_total_steps, total_steps)                
            memo[state] = min_total_steps
            return min_total_steps
        return dp(0, 0)
