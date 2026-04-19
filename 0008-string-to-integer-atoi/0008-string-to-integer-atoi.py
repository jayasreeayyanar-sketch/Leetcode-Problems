class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            if sign * num < INT_MIN:
                return INT_MIN
            if sign * num > INT_MAX:
                return INT_MAX
            
            i += 1
        
        return sign * num