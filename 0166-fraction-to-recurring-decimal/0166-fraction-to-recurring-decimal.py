class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"            
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        num = abs(numerator)
        den = abs(denominator)        
        res.append(str(num // den))        
        remainder = num % den
        if remainder == 0:
            return "".join(res)            
        res.append(".")
        seen_remainders = {}        
        while remainder != 0:
            if remainder in seen_remainders:
                res.insert(seen_remainders[remainder], "(")
                res.append(")")
                break
            seen_remainders[remainder] = len(res)            
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den            
        return "".join(res)
