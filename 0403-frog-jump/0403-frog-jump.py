class Solution(object):
    def canCross(self, stones):
        stone_to_idx = {stone: i for i, stone in enumerate(stones)}
        target = stones[-1]
        memo = {}        
        def dfs(curr_idx, k):
            if stones[curr_idx] == target:
                return True                
            state = (curr_idx, k)
            if state in memo:
                return memo[state]                
            curr_pos = stones[curr_idx]
            for next_jump in (k - 1, k, k + 1):
                if next_jump > 0:
                    next_pos = curr_pos + next_jump
                    if next_pos in stone_to_idx:
                        if dfs(stone_to_idx[next_pos], next_jump):
                            memo[state] = True
                            return True                            
            memo[state] = False
            return False
        if len(stones) > 1 and stones[1] != 1:            return False
            
        return dfs(1, 1)