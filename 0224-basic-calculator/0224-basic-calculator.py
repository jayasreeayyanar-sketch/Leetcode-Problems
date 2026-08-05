class Solution(object):
    def calculate(self, s):        
        stack = []
        current_result = 0
        sign = 1  
        i = 0
        n = len(s)        
        while i < n:
            char = s[i]            
            if char.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                current_result += sign * num
                i -= 1                
            elif char == '+':
                sign = 1
                
            elif char == '-':
                sign = -1                
            elif char == '(':
                stack.append(current_result)
                stack.append(sign)
                current_result = 0
                sign = 1                
            elif char == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                current_result = prev_result + (prev_sign * current_result)                
            i += 1            
        return current_result