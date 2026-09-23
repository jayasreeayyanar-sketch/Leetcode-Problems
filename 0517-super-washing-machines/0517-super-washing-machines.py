class Solution(object):
    def findMinMoves(self, machines):
        total_dresses = sum(machines)
        n = len(machines)
        if total_dresses % n != 0:
            return -1
            
        target = total_dresses // n
        max_moves = 0
        current_balance = 0
        
        for dresses in machines:
            current_balance += dresses - target
            
            max_moves = max(max_moves, abs(current_balance), dresses - target)
            
        return max_moves
