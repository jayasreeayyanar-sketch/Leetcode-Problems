class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]        
        words = []
        i = 0
        while num > 0:
            if num % 1000 != 0:
                segment_words = self._helper(num % 1000)
                if self.THOUSANDS[i]:
                    segment_words += " " + self.THOUSANDS[i]
                words.append(segment_words)
            num //= 1000
            i += 1
        return " ".join(reversed(words)).strip()

    def _helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_20[num]
        elif num < 100:
            remainder = self._helper(num % 10)
            return self.TENS[num // 10] + (" " + remainder if remainder else "")
        else:
            remainder = self._helper(num % 100)
            return self.LESS_THAN_20[num // 100] + " Hundred" + (" " + remainder if remainder else "")