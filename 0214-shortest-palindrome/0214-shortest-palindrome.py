class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return ""
        combined = s + "#" + s[::-1]
        n = len(combined)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i-1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j-1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        palindrome_len = lps[-1]
        suffix_to_add = s[palindrome_len:][::-1]
        return suffix_to_add + s
