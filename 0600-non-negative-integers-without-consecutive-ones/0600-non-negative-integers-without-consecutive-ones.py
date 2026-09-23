class Solution(object):
    def findIntegers(self, n):
        binary = bin(n)[2:]
        length = len(binary)
        
        f = [0] * (length + 1)
        f[0] = 1
        f[1] = 2
        for i in range(2, length + 1):
            f[i] = f[i-1] + f[i-2]
            
        result = 0
        prev_bit = 0
        for i in range(length):
            if binary[i] == '1':
                result += f[length - 1 - i]
                
                if prev_bit == 1:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0
                
        return result + 1
