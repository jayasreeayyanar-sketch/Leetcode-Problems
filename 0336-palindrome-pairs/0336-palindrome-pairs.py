id="s2f9k1"
class Solution(object):
    def palindromePairs(self, words):
        result = []
        word_map = {}
        for i, word in enumerate(words):
            word_map[word[::-1]] = i

        def isPalindrome(s):
            return s == s[::-1]
        for i, word in enumerate(words):
            length = len(word)
            for j in range(length + 1):
                left = word[:j]
                right = word[j:]
                if isPalindrome(left):
                    if right in word_map and word_map[right] != i:
                        result.append([word_map[right], i])
                if j != length and isPalindrome(right):
                    if left in word_map and word_map[left] != i:
                        result.append([i, word_map[left]])
        return result