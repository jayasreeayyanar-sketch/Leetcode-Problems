class Solution(object):
    def addOperators(self, num, target):
        res = []        
        def backtrack(index, prev_op, current_val, path_segments):
            if index == len(num):
                if current_val == target:
                    res.append("".join(path_segments))
                return
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                sub_str = num[index:i+1]
                curr_op = int(sub_str)
                if index == 0:
                    path_segments.append(sub_str)
                    backtrack(i + 1, curr_op, curr_op, path_segments)
                    path_segments.pop()
                else:
                    path_segments.append('+' + sub_str)
                    backtrack(i + 1, curr_op, current_val + curr_op, path_segments)
                    path_segments.pop()
                    path_segments.append('-' + sub_str)
                    backtrack(i + 1, -curr_op, current_val - curr_op, path_segments)
                    path_segments.pop()
                    path_segments.append('*' + sub_str)
                    backtrack(i + 1, prev_op * curr_op, current_val - prev_op + (prev_op * curr_op), path_segments)
                    path_segments.pop()                    
        backtrack(0, 0, 0, [])
        return res