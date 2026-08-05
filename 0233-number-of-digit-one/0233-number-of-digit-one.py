class Solution(object):
    def countDigitOne(self, n):       
        if n <= 0:
            return 0            
        count = 0
        factor = 1        
        while factor <= n:
            higher_numbers = n // (factor * 10)
            current_digit = (n // factor) % 10
            lower_numbers = n % factor
            count += higher_numbers * factor
            if current_digit == 1:
                count += lower_numbers + 1
            elif current_digit > 1:
                count += factor
            factor *= 10            
        return count