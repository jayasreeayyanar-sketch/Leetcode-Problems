from collections import Counter

class Solution(object):
    def findMinStep(self, board, hand):
        hand_count = Counter(hand)
        memo = {}        
        def remove_consecutive(s):
            stack = [] 
            for char in s:
                if stack and stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    if stack and stack[-1][1] >= 3:
                        stack.pop()
                        if stack and stack[-1][0] == char:
                            stack[-1][1] += 1
                            continue
                    stack.append([char, 1])
            if stack and stack[-1][1] >= 3:
                stack.pop()
            return "".join(char * count for char, count in stack)
        def dfs(curr_board, curr_hand):
            if not curr_board:
                return 0
            hand_state = tuple(sorted(curr_hand.items()))
            state = (curr_board, hand_state)
            if state in memo:
                return memo[state]                
            min_steps = float('inf')
            i = 0
            while i <= len(curr_board):
                for color in list(curr_hand.keys()):
                    if curr_hand[color] <= 0:
                        continue
                    is_valid_move = False
                    if i < len(curr_board) and curr_board[i] == color:
                        is_valid_move = True
                    elif i > 0 and curr_board[i-1] == color:
                        is_valid_move = True
                    elif i > 0 and i < len(curr_board) and curr_board[i-1] == curr_board[i] and curr_board[i] != color:
                        is_valid_move = True                        
                    if not is_valid_move:
                        continue
                    next_board = curr_board[:i] + color + curr_board[i:]
                    next_board = remove_consecutive(next_board)
                    curr_hand[color] -= 1
                    if curr_hand[color] == 0:
                        del curr_hand[color]                        
                    steps = dfs(next_board, curr_hand)
                    if steps != -1:
                        min_steps = min(min_steps, 1 + steps)
                    curr_hand[color] += 1                    
                i += 1                
            memo[state] = min_steps if min_steps != float('inf') else -1
            return memo[state]
        return dfs(board, hand_count)